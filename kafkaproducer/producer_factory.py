from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro

_producer_cache = {}

def get_producer_for_topic(topic: str):
    global _producer_cache

    if topic in _producer_cache:
        return _producer_cache[topic]

    # Define key/value schemas for the topic
    key_schema = avro.loads("""{"type": "string"}""")
    value_schema = get_value_schema_for_topic(topic)

    # Create a schema-aware AvroProducer
    producer = AvroProducer({
        'bootstrap.servers': 'your-broker:9092',
        'schema.registry.url': 'http://schema-registry:8081',
        'linger.ms': 10,
        'batch.num.messages': 500,
    }, default_key_schema=key_schema, default_value_schema=value_schema)

    _producer_cache[topic] = producer
    return producer

def get_value_schema_for_topic(topic: str):
    # Customize per topic schema
    if topic == "user-updates":
        return avro.loads("""
        {
            "type": "record",
            "name": "User",
            "fields": [
                {"name": "id", "type": "string"},
                {"name": "email", "type": "string"}
            ]
        }
        """)
    elif topic == "order-events":
        return avro.loads("""
        {
            "type": "record",
            "name": "Order",
            "fields": [
                {"name": "order_id", "type": "string"},
                {"name": "amount", "type": "float"}
            ]
        }
        """)
    else:
        raise ValueError(f"No schema defined for topic {topic}")
