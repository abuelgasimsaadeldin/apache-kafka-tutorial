from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('farmers', b'Hello from the Python producer')
time.sleep(10)