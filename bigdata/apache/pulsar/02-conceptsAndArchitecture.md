# Concepts and Architecture

## Messaging

Pulsar is built on the publish-subscribe pattern (often abbreviated to pub-sub).

### Messages

| Component | Description |
| ------ | ------ |
| Value / data payload | The data carried by the message. All Pulsar messages contain raw bytes, although message data can also conform to data schemas. |
| Key | The key (string type) of the message. It is a short name of message key or partition key. Messages are optionally tagged with keys, which is useful for features like topic compaction. |
| Properties | An optional key/value map of user-defined properties. |
| Producer name | The name of the producer who produces the message. If you do not specify a producer name, the default name is used. |
| Topic name | The name of the topic that the message is published to. |
| Schema version | The version number of the schema that the message is produced with. |
| Sequence ID | Each Pulsar message belongs to an ordered sequence on its topic. The sequence ID of a message is initially assigned by its producer, indicating its order in that sequence, and can also be customized. Sequence ID can be used for message deduplication. If `brokerDeduplicationEnabled` is set to `true`, the sequence ID of each message is unique within a producer of a topic (non-partitioned) or a partition. |
| Message ID | The message ID of a message is assigned by bookies as soon as the message is persistently stored. Message ID indicates a message's specific position in a ledger and is unique within a Pulsar cluster. |
| Publish time | The timestamp of when the message is published. The timestamp is automatically applied by the producer. |
| Event time | An optional timestamp attached to a message by applications. For example, applications attach a timestamp on when the message is processed. If nothing is set to event time, the value is 0. |

Messages can be acknowledged in one of the following two ways:

- Being acknowledged individually. With individual acknowledgment, the consumer acknowledges each message and sends an acknowledgment request to the broker.

    ```java
    consumer.acknowledge(msg);
    ```

- Being acknowledged cumulatively. With cumulative acknowledgment, the consumer **only** acknowledges the last message it received. All messages in the stream up to (and including) the provided message are not redelivered to that consumer.

    ```java
    consumer.acknowledgeCumulative(msg);
    ```

#### Negative acknowledgment

Be aware that negative acknowledgments on ordered subscription types, such as Exclusive, Failover and Key_Shared, might cause failed messages being sent to consumers out of the original order.

#### Retry letter topic

![Alt text](https://pulsar.apache.org/assets/images/retry-letter-topic-5304f63457e6c17da20d0de7b6897a5b.svg)

By default, automatic retry is disabled. You can set `enableRetry` to `true` to enable automatic retry on the consumer.

The default retry letter topic uses this format:

```text
<topicname>-<subscriptionname>-RETRY
```

#### Dead letter topic

The default dead letter topic uses this format:

```text
<topicname>-<subscriptionname>-DLQ
```

#### Compression

compression types:

- [LZ4](https://github.com/lz4/lz4)
- [ZLIB](https://zlib.net/)
- [ZSTD](https://facebook.github.io/zstd/)
- [SNAPPY](https://google.github.io/snappy/)

The sample code below shows how to enable compression type for a producer:

```java
client.newProducer()
    .topic("topic-name")
    .compressionType(CompressionType.LZ4)
    .create();
```

#### Batching

In Pulsar, batches are tracked and stored as single units rather than as individual messages. Consumers unbundle a batch into individual messages. However, scheduled messages (configured through the `deliverAt` or the `deliverAfter` parameter) are always sent as individual messages even when batching is enabled.

In general, a batch is acknowledged when all of its messages are acknowledged by a consumer. It means that when not all batch messages are acknowledged, then unexpected failures, negative acknowledgments, or acknowledgment timeouts can result in a redelivery of all messages in this batch.

To avoid redelivering acknowledged messages in a batch to the consumer, Pulsar introduces batch index acknowledgment since Pulsar 2.6.0. When batch index acknowledgment is enabled, the consumer filters out the batch index that has been acknowledged and sends the batch index acknowledgment request to the broker. The broker maintains the batch index acknowledgment status and tracks the acknowledgment status of each batch index to avoid dispatching acknowledged messages to the consumer. The batch is deleted when all indices of the messages in it are acknowledged.

By default, batch index acknowledgment is disabled (`acknowledgmentAtBatchIndexLevelEnabled=false`). You can enable batch index acknowledgment by setting the `acknowledgmentAtBatchIndexLevelEnabled` parameter to `true` at the broker side. **Enabling batch index acknowledgment results in more memory overheads.**

Batch index acknowledgment must also be enabled in the consumer by calling .enableBatchIndexAcknowledgment(true);

For example:

```java
Consumer<byte[]> consumer = pulsarClient.newConsumer()
        .topic(topicName)
        .subscriptionName(subscriptionName)
        .subscriptionType(subType)
        .enableBatchIndexAcknowledgment(true)
        .subscribe();
```

#### Chunking

Message chunking enables Pulsar to process large payload messages by splitting the message into chunks at the producer side and aggregating chunked messages at the consumer side.

With message chunking enabled, when the size of a message exceeds the allowed maximum payload size (the `maxMessageSize` parameter of broker), the workflow of messaging is as follows:

- The producer splits the original message into chunked messages and publishes them with chunked metadata to the broker separately and in order.
- The broker stores the chunked messages in one managed ledger in the same way as that of ordinary messages, and it uses the `chunkedMessageRate` parameter to record chunked message rate on the topic.
- The consumer buffers the chunked messages and aggregates them into the receiver queue when it receives all the chunks of a message.
- The client consumes the aggregated message from the receiver queue.

> **Note**
>
> - Chunking is only available for persistent topics.
> - Chunking cannot be enabled simultaneously with batching. Before enabling chunking, you need to disable batching.

![Alt text](https://pulsar.apache.org/assets/images/chunking-02-50ca285dd380b4bbecc01774655ead49.png)

> **Note**
>
> In this case, interwoven chunked messages may bring some memory pressure to the consumer because the consumer keeps a separate buffer for each large message to aggregate all its chunks in one message. You can limit the maximum number of chunked messages a consumer maintains concurrently by configuring the `maxPendingChunkedMessage` parameter. When the threshold is reached, the consumer drops pending messages by silently acknowledging them or asking the broker to redeliver them later, optimizing memory utilization.
