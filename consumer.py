from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'farm',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='farm-consumer-group'
)

for message in consumer:
    print(message)
