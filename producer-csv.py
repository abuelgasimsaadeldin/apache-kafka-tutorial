from kafka import KafkaProducer
import csv
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092')

with open('Kafka-Data/sensors.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        producer.send('farmers', json.dumps(row).encode('utf-8'))
        print(row)
        time.sleep(1)
