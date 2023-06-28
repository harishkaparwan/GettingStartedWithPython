import kafka

def connect_to_kafka():
    """Connects to Kafka using SSL."""
    bootstrap_servers = "localhost:9093"
    ssl_truststore_location = "/path/to/truststore.pem"
    ssl_truststore_password = "password"

    consumer = kafka.KafkaConsumer("my-topic",
                                  bootstrap_servers=bootstrap_servers,
                                  ssl_truststore_location=ssl_truststore_location,
                                  ssl_truststore_password=ssl_truststore_password)

    return consumer


if __name__ == "__main__":
    consumer = connect_to_kafka()
    for message in consumer:
        print(message)
