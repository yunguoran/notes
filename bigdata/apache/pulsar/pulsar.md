# Apache Pulsar

## Get Started

### Run Rulsar locally

#### Download Pulsar distribution

```shell
wget https://archive.apache.org/dist/pulsar/pulsar-3.0.0/apache-pulsar-3.0.0-bin.tar.gz
tar xvfz apache-pulsar-3.0.0-bin.tar.gz
cd apache-pulsar-3.0.0
ls -1F
```

#### Start a Pulsar standalone cluster

```shell
bin/pulsar standalone
```

- To run the service as a background process, you can use the `bin/pulsar-daemon start standalone` command.
- The `public/default` namespace is created when you start a Pulsar cluster. This namespace is for development purposes. All Pulsar topics are managed within namespaces.

#### Create a topic

Pulsar stores messages in topics. To create a new topic, run this command:

```shell
bin/pulsar-admin topics create persistent://public/default/my-topic
```

#### Write messages to the topic

You can use the pulsar command line tool to write messages to a topic. This is useful for experimentation, but in practice you'll use the Producer API in your application code, or Pulsar IO connectors for pulling data in from other systems to Pulsar.

Run this command to produce a message:

```shell
bin/pulsar-client produce my-topic --messages 'Hello Pulsar!'
```

#### Read messages from the topic

run this command to launch the consumer and read those messages back:

```shell
bin/pulsar-client consume my-topic -s 'my-subscription' -p Earliest -n 0
```

`Earliest` means consuming from the earliest unconsumed message. `-n` configures the number of messages to consume, `0` means to consume forever.

This is useful for experimenting with messages, but in practice you'll use the Consumer API in your application code, or Pulsar IO connectors for reading data from Pulsar to push to other systems.

You'll see the messages you produce in the previous step:

```text
----- got message -----
key:[null], properties:[], content:Hello Pulsar!
```

#### Write some more messages

Now open a new terminal window and produce more messages. The default message separator is `,`:

```shell
bin/pulsar-client produce my-topic --messages "$(seq -s, -f 'Message NO.%g' 1 10)"
```

### Run Pulsar in Docker

#### Start Pulsar in Docker

```shell
docker run -it -p 6650:6650 -p 8080:8080 --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:3.0.0 bin/pulsar standalone
```

If you want to change Pulsar configurations and start Pulsar, run the following command by passing environment variables with the PULSAR_PREFIX_ prefix. See [default configuration file](https://github.com/apache/pulsar/blob/e6b12c64b043903eb5ff2dc5186fe8030f157cfc/conf/standalone.conf) for more details.

```shell
docker run -it -e PULSAR_PREFIX_xxx=yyy -p 6650:6650  -p 8080:8080 --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:2.10.0 sh -c "bin/apply-config-from-env.py conf/standalone.conf && bin/pulsar standalone"
```

To perform a health check, you can use the `bin/pulsar-admin brokers healthcheck` command.

#### Use Pulsar in Docker

If you're running a local standalone cluster, you can use one of these root URLs to interact with your cluster:

- <pulsar://localhost:6650>
- <http://localhost:8080>

get started with Pulsar by using the [Python client API](https://pulsar.apache.org/api/python/3.2.x/).

Install the Pulsar Python client library directly from PyPI:

```shell
pip install pulsar-client
```

Create a consumer and subscribe to the topic:

```python
import pulsar

client = pulsar.Client('pulsar://localhost:6650')
consumer = client.subscribe('my-topic', subscription_name='my-sub')

while True:
    msg = consumer.receive()
    print("Received message: '%s'" % msg.data())
    consumer.acknowledge(msg)

client.close()
```

Start a producer to send some test messages:

```python
import pulsar

client = pulsar.Client('pulsar://localhost:6650')
producer = client.create_producer('my-topic')

for i in range(10):
    producer.send(('hello-pulsar-%d' % i).encode('utf-8'))

client.close()
```

#### Get the topic statistics

In the simplest example, you can use curl to probe the stats for a particular topic:

```shell
curl http://localhost:8080/admin/v2/persistent/public/default/my-topic/stats | python -m json.tool
```

### [Run Pulsar in Kubernetes](https://pulsar.apache.org/docs/3.0.x/getting-started-helm/)

### [Run Pulsar locally with Docker Compos](https://pulsar.apache.org/docs/3.0.x/getting-started-docker-compose/)

## Concepts and Architecture

### Messaging

Pulsar is built on the publish-subscribe pattern (often abbreviated to pub-sub).
