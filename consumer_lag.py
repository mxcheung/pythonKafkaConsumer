from confluent_kafka import Consumer, KafkaError, TopicPartition

def get_consumer_group_lag(bootstrap_servers, group_id, topic):
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'group.id': group_id,
        'auto.offset.reset': 'latest',
        'enable.auto.commit': False
    }

    consumer = Consumer(conf)

    # Get the partitions for the specified topic
    metadata = consumer.list_topics(topic)
    partitions = metadata.topics[topic].partitions

    # Assign the topic and partitions to the consumer
    consumer.assign([TopicPartition(topic, partition) for partition in partitions])

    # Get the current positions (offsets) for each partition
    current_offsets = consumer.committed(consumer.assignment())

    # Get the latest available positions (offsets) for each partition
    end_offsets = consumer.get_watermark_offsets(consumer.assignment())

    # Calculate the consumer group lag for each partition
    lag_per_partition = {
        tp.partition: end_offsets[tp] - current_offsets[tp]
        for tp in consumer.assignment()
    }

    consumer.close()

    return lag_per_partition

# Example usage
bootstrap_servers = 'localhost:9092'
group_id = 'my_consumer_group'
topic = 'my_topic'

consumer_group_lag = get_consumer_group_lag(bootstrap_servers, group_id, topic)
print(consumer_group_lag)
