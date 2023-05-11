from confluent_kafka import Consumer, KafkaError

def get_consumer_group_lag(bootstrap_servers, group_id, topic):
    conf = {
        'bootstrap.servers': bootstrap_servers,
        'group.id': group_id,
        'auto.offset.reset': 'latest',
        'enable.auto.commit': False
    }

    consumer = Consumer(conf)

    # Assign the topic and partitions to the consumer
    consumer.assign([TopicPartition(topic, partition) for partition in consumer.partitions_for_topic(topic)])

    # Get the current positions (offsets) and timestamps for each partition
    current_positions = consumer.committed(consumer.assignment())
    timestamps = consumer.offsets_for_times(current_positions)

    # Get the latest available positions (offsets) and timestamps for each partition
    end_offsets = consumer.get_watermark_offsets(consumer.assignment())
    end_timestamps = consumer.offsets_for_times(end_offsets)

    # Calculate the consumer group lag and last message creation timestamp for each partition
    lag_per_partition = {}
    last_message_timestamps = {}
    for tp in consumer.assignment():
        lag_per_partition[tp.partition] = end_offsets[tp] - current_positions[tp]
        last_message_timestamps[tp.partition] = end_timestamps[tp].timestamp if end_timestamps[tp] else None

    consumer.close()

    return lag_per_partition, last_message_timestamps

# Example usage
bootstrap_servers = 'localhost:9092'
group_id = 'my_consumer_group'
topic = 'my_topic'

consumer_group_lag, last_message_timestamps = get_consumer_group_lag(bootstrap_servers, group_id, topic)
print('Consumer Group Lag:', consumer_group_lag)
print('Last Message Timestamps:', last_message_timestamps)
