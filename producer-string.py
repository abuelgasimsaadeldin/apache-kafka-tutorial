from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('test', b'Hello again2 from the Python producer')
time.sleep(20)