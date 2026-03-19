from confluent_kafka import Consumer

# configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-group2',
    'auto.offset.reset': 'earliest'
}

#create consumer instance
consumer=Consumer(conf)

#subscribe to topic
consumer.subscribe(['test-topic'])

#Loop to consume messages
try:
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            print(f"Error: {msg.error()}")
        else:
            print(f"Received: {msg.value().decode('utf-8')} partition={msg.partition()} offset={msg.offset()}")

except KeyboardInterrupt:
    pass

finally:
    consumer.close()