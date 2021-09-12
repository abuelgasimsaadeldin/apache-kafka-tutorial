from kafka import KafkaProducer
import time

# Start up producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Send a String message in the form of bytes to the Kafka Topic 'farm'
producer.send('farm', b'Hello from the Python producer')
time.sleep(10)
