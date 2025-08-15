# pythonKafkaConsumer
Python Kafka Consumer

# Objective
1. use confluent kafka ssl
2. Kafka consumer
3. Parse JSON payload
4. Execute command within payload
5. Print the exit code of the command


#Errors

AttributeError: 'cimpl.Consumer' object has no attribute 'partitions_for_topic'


Why can't offset retention be changed?

Consumer offsets are tracked in Kafka's internal topic (__consumer_offsets) and managed at the broker level, which Confluent Cloud restricts to maintain managed service stability and consistency.

This topic-level control is intentionally separated from broker-level settings like offsets.retention.minutes, and Confluent reserves tight control over broker configs in


You cannot change the retention period for consumer offsets (i.e., offsets.retention.minutes) in Confluent Cloud on Basic, Standard, Enterprise, or Freight clusters—it’s not configurable by users

retention period for consumer offsets
