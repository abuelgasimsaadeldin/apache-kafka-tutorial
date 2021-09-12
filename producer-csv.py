from kafka import KafkaProducer
import csv
import json
import time

# Start up producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Read the CSV file
with open('Kafka-Data/sensors.csv', 'r') as file:
    reader = csv.reader(file)

    # Send record by record of CSV file to the Kafka topic 'farm'
    for row in reader:
        producer.send('farm', json.dumps(row).encode('utf-8'))
        print(row)
        time.sleep(1)
