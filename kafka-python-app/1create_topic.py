from confluent_kafka.admin import AdminClient, NewTopic

# 1. Admin client config
admin = AdminClient({
    'bootstrap.servers': 'localhost:9092'
})

# 2. Define topic
topic = NewTopic(
    topic="my-topic-1",
    num_partitions=3,
    replication_factor=1
)

# 3. Create topic
futures = admin.create_topics([topic])

# 4. Check result
for topic_name, future in futures.items():
    try:
        future.result()
        print(f"Topic '{topic_name}' created")
    except Exception as e:
        print(f"Failed to create topic '{topic_name}': {e}")