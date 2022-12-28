from kafka import KafkaConsumer

# Consumer test
# Set the Kafka consumer settings
consumer = KafkaConsumer('trends', bootstrap_servers=['localhost:9092'])

# Iterate through the messages in the Kafka topic
for message in consumer:
    print(message.value)
