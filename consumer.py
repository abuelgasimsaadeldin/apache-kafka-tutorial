from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='test-consumer-group'
)

for message in consumer:
    print(message)