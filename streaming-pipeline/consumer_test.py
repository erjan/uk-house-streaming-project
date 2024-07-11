from kafka import KafkaConsumer

# Kafka broker connection details
bootstrap_servers = 'splendid-goshawk-5336-us1-kafka.upstash.io:9092'
sasl_mechanism = 'SCRAM-SHA-256'
security_protocol = 'SASL_SSL'
sasl_plain_username = 'c3BsZW5kaWQtZ29zaGF3ay01MzM2JDCzi5Tfmu0-6nTKYRO_seo8KHg2wJ4rH0k'
sasl_plain_password = 'MmFkOWViYmItMGVjYi00MWI3LTlkNmYtYTYyZmZkMjNjZjA2'

# Create the Kafka consumer
consumer = KafkaConsumer(
    bootstrap_servers=bootstrap_servers,
    sasl_mechanism=sasl_mechanism,
    security_protocol=security_protocol,
    sasl_plain_username=sasl_plain_username,
    sasl_plain_password=sasl_plain_password,
    auto_offset_reset='latest'
)

# Subscribe to the Kafka topic
consumer.subscribe(['company_house'])

# Consume messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")