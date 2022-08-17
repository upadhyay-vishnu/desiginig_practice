import json
from kafka import KafkaProducer, KafkaConsumer

TOPIC = "food_order"

consumer = KafkaConsumer(TOPIC, bootstrap_servers=['localhost:9092'], api_version=(0,11,5))

print("start listening the Producer: ")

while True:
	for message in consumer:
		print("new feed: ")
		print(json.loads(message.value.decode()))
