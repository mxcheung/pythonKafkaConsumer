from producer_factory import get_producer_for_topic

def message_handler(topic: str, key: str, value: dict):
    producer = get_producer_for_topic(topic)

    producer.produce(
        topic=topic,
        key=key,
        value=value
    )
    producer.poll(0)
