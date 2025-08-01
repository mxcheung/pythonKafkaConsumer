# kafka_producer.py
from confluent_kafka import Producer

_kafka_producer = None

def get_kafka_producer():
    global _kafka_producer
    if _kafka_producer is None:
        _kafka_producer = Producer({
            'bootstrap.servers': 'your-broker:9092',
            'linger.ms': 10,
            'batch.num.messages': 1000,
            # Add retries, acks, etc. if needed
        })
    return _kafka_producer
