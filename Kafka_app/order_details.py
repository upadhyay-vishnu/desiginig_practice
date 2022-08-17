"""
Building a simple Food App with Kafka
"""
import json
import time
from kafka import KafkaProducer

TOPIC = "food_order"
ORDER_LIMIT = 15

print("creating new order every 1 sec")
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0,11,5))

for i in range(15):
	data = {
		"order_id": i,
		"customer_id": f"abc-{i}",
		"price": 100,
		"order": ["Sandwich", "Burger"]
	}

	producer.send(topic=TOPIC, value=json.dumps(data).encode('utf-8'))

	print(f"sending data for order-{i}")
	time.sleep(2)
