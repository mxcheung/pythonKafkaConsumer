# message_handler.py
from kafka_producer import get_kafka_producer

def delivery_report(err, msg):
    if err:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()}")

def message_handler(msg):
    producer = get_kafka_producer()
    transformed = transform(msg)
    producer.produce(
        topic="output-topic",
        key=None,
        value=transformed,
        callback=delivery_report
    )
    producer.poll(0)  # Lightweight call for delivery handling

def transform(msg):
    return msg.upper()
