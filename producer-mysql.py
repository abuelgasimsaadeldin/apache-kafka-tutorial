import time

from kafka import KafkaProducer
import mysql.connector
import json

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd="skymind",
    database="farmers")

mycursor = db.cursor()

producer = KafkaProducer(bootstrap_servers='localhost:9092')

mycursor.execute("SELECT * FROM farmers")

for x in mycursor:
    producer.send('farmers', json.dumps(x).encode('utf-8'))
    print(x)
    time.sleep(1)
