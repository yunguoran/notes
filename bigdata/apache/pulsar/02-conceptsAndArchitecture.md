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

### Topics

Topic names are URLs that have a well-defined structure:

```text
{persistent|non-persistent}://tenant/namespace/topic
```

| Topic name component | Description|
| ------ | ------ |
| persistent / non-persistent | This identifies the type of topic. Pulsar supports two kind of topics: persistent and | non-persistent. The default is persistent, so if you do not specify a type, the topic is persistent. With persistent topics, all messages are durably persisted on disks (if the broker is not standalone, messages are durably persisted on multiple disks), whereas data for non-persistent topics is not persisted to storage disks.
| tenant | The topic tenant within the instance. Tenants are essential to multi-tenancy in Pulsar, and spread across | clusters.
| namespace | The administrative unit of the topic, which acts as a grouping mechanism for related topics. Most topic | configuration is performed at the namespace level. Each tenant has one or more namespaces.
| topic | The final part of the name. Topic names have no special meaning in a Pulsar instance.|

### Namespaces

A namespace is a logical nomenclature within a tenant.

### Subscriptions

A subscription is a named configuration rule that determines how messages are delivered to consumers.

![pulsarSubscriptionTypes](./images/pulsarSubscriptionTypes.png)

#### Subscription types

Exclusive(default)

In the Exclusive type, only a single consumer is allowed to attach to the subscription.

![Alt text](https://pulsar.apache.org/assets/images/pulsar-exclusive-subscriptions-b3304e5b293d0a6da17637735fcb1650.svg)

Failover

- In the Failover type, multiple consumers can attach to the same subscription.
- A master consumer is picked for a non-partitioned topic or each partition of a partitioned topic and receives messages.
- When the master consumer disconnects, all (non-acknowledged and subsequent) messages are delivered to the next consumer in line.

Failover | Partitioned topics

If the number of partitions in a partitioned topic is less than the number of consumers:

![Alt text](https://pulsar.apache.org/assets/images/pulsar-failover-subscriptions-4-74e4b825d13ce1197c1281819fe14554.svg)

If the number of partitions in a partitioned topic is greater than the number of consumers:

![Alt text](https://pulsar.apache.org/assets/images/pulsar-failover-subscriptions-1-bb15a6e2f6373dc1f20eecf1779ee0c7.svg)

Failover | Non-partitioned topics

If there is one non-partitioned topic:

![Alt text](https://pulsar.apache.org/assets/images/pulsar-failover-subscriptions-2-1f72791597afa07fa987ae1f7bc5cd42.svg)

If there are multiple non-partitioned topics:

![Alt text](https://pulsar.apache.org/assets/images/pulsar-failover-subscriptions-3-2b2e00ef5ee525ca7c1fd21dcd67e328.svg)

Shared

In shared or round robin type, multiple consumers can attach to the same subscription. Messages are delivered in a round-robin distribution across consumers, and any given message is delivered to only one consumer. When a consumer disconnects, all the messages that were sent to it and not acknowledged will be rescheduled for sending to the remaining consumers.

![Alt text](https://pulsar.apache.org/assets/images/pulsar-shared-subscriptions-c368030415b85eb3ef96448f79e87a58.svg)

Key_Shared

In the Key_Shared type, multiple consumers can attach to the same subscription. Messages are delivered in distribution across consumers and messages with the same key or same ordering key are delivered to only one consumer. No matter how many times the message is re-delivered, it is delivered to the same consumer.

![Alt text](https://pulsar.apache.org/assets/images/pulsar-key-shared-subscriptions-17bf12baab858b4ac0e66b9207bf4503.svg)

There are three types of mapping algorithms dictating how to select a consumer for a given message key (or ordering key):

- [Sticky](https://pulsar.apache.org/docs/3.0.x/concepts-messaging/#sticky)
- [Auto-split Hash Range](https://pulsar.apache.org/docs/3.0.x/concepts-messaging/#auto-split-hash-range)
- [Auto-split Consistent Hashing](https://pulsar.apache.org/docs/3.0.x/concepts-messaging/#auto-split-consistent-hashing)

##### Batching for Key Shared Subscriptions

> **Note**
>
> When the consumers are using the Key_Shared subscription type, you need to disable batching or use key-based batching for the producers.

There are two reasons why the key-based batching is necessary for the Key_Shared subscription type:

- The broker dispatches messages according to the keys of the messages, but the default batching approach might fail to pack the messages with the same key to the same batch.
- Since it is the consumers instead of the broker who dispatch the messages from the batches, the key of the first message in one batch is considered as the key to all messages in this batch, thereby leading to context errors.

#### Subscription modes

- Durable(default)
- NonDurable

### Multi-topic subscriptions

> *Note*
>
> - When subscribing to multiple topics by regex, all topics must be in the same namespace.
> - No ordering guarantees across multiple topics When a producer sends messages to a single topic,

### Partitioned topics

![Alt text](./images/partitionedTopics.png)

#### Routing modes

- RoundRobinPartition
- SinglePartition
- CustomPartition

#### Ordering guarantee

 | Ordering guarantee | Description | Routing Mode and Key |
 | ------ | ------ | ------ |
 | Per-key-partition | All the messages with the same key will be in order and be placed in same partition. | Use either SinglePartition or RoundRobinPartition mode, and Key is provided by each message. |
 | Per-producer | All the messages from the same producer will be in order. | Use SinglePartition mode, and no Key is provided for each message. |

#### Hashing scheme

- JavaStringHash
- Murmur3_32Hash

Please pay attention that `JavaStringHash` is not useful when producers can be from different multiple language clients, under this use case, it is recommended to use `Murmur3_32Hash`.

### Non-persistent topics

Pulsar also, however, supports non-persistent topics, which are topics on which messages are never persisted to disk and live only in memory. When using non-persistent delivery, killing a Pulsar broker or disconnecting a subscriber to a topic means that all in-transit messages are lost on that (non-persistent) topic, meaning that clients may see message loss.

Non-persistent topics have names of this form:

```text
non-persistent://tenant/namespace/topic
```

### System topic

System topic is a predefined topic for internal use within Pulsar. It can be either a persistent or non-persistent topic.

### Message retention and expiry

- Message retention enables you to store messages that have been acknowledged by a consumer.
- Message expiry enables you to set a time to live (TTL) for messages that have not yet been acknowledged.

### Message deduplication

![Alt text](https://pulsar.apache.org/assets/images/message-deduplication-854309d2abf6e9ba16d2a3f090e59ace.svg)
