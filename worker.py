from confluent_kafka import Consumer, KafkaError
import json
import subprocess

conf = {
    'bootstrap.servers': '<KAFKA_BOOTSTRAP_SERVERS>',
    'security.protocol': 'ssl',
    'ssl.ca.location': '<CA_CERT_FILE>',
    'ssl.certificate.location': '<CLIENT_CERT_FILE>',
    'ssl.key.location': '<CLIENT_KEY_FILE>',
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)

consumer.subscribe(['my-topic'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            print('End of partition reached')
        else:
            print('Error while consuming message: {}'.format(msg.error()))
        continue

    try:
        payload = json.loads(msg.value())
        job_id = payload['job_id']
        command = payload['command']
        result = subprocess.run(command, shell=True)
        print('Job ID: {}, Exit code of command {}: {}'.format(job_id, command, result.returncode))
    except Exception as e:
        print('Error while processing message: {}'.format(str(e)))

consumer.close()
