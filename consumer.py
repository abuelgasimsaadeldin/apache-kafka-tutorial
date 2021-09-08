from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'farmers',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='farmers-consumer-group'
)

for message in consumer:
    print(message)