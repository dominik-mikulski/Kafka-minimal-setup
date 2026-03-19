from confluent_kafka import Producer

# callback function called on delivery report
def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Delivered to {msg.topic()} [{msg.partition()}]")

# Configuration
conf={'bootstrap.servers':'localhost:9092'}

# Create Producer instance
producer=Producer(conf)

# Send msg to topic
producer.produce('test-topic', key='user10', value='12. Hello Kafka!',callback=delivery_report)

# flush data
producer.flush()