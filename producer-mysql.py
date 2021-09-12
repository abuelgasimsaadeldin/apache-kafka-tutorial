from kafka import KafkaProducer
import mysql.connector
import json
import time

# Establish a connection with the MySQL Database
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="skymind",
    database="farmers")

# Create cursor object to communicate with MySQL database
mycursor = db.cursor()

# Start up Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Select all records from the Database
mycursor.execute("SELECT * FROM farmers")

for x in mycursor:
    # Send data record by record from database to Kafka topic 'farm'
    producer.send('farm', json.dumps(x).encode('utf-8'))
    print(x)
    time.sleep(1)
