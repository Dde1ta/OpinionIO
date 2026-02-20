from fastkafka import FastKafka
import socket

# Define your local broker config
kafka_brokers = {
    "localhost": {
        "url": "localhost",
        "description": "Local development Kafka broker",
        "port": 9092,
    }
}

# Initialize the FastKafka app
# We will tie this to the FastAPI lifespan later
kafka_app = FastKafka(
    kafka_brokers=kafka_brokers,
    client_id=socket.gethostname()
)
