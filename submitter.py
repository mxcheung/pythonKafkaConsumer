from confluent_kafka import Producer
import json

conf = {
    'bootstrap.servers': '<KAFKA_BOOTSTRAP_SERVERS>',
    'security.protocol': 'ssl',
    'ssl.ca.location': '<CA_CERT_FILE>',
    'ssl.certificate.location': '<CLIENT_CERT_FILE>',
    'ssl.key.location': '<CLIENT_KEY_FILE>',
}

producer = Producer(conf)

payload = {
    'job_id': '1234',
    'command': 'echo "Hello World!"'
}
json_payload = json.dumps(payload).encode('utf-8')

producer.produce('my-topic', value=json_payload)
producer.flush()

print('Message sent to Kafka')
