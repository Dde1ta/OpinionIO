from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.consumes(topic="NEW_TASK")
async def test(msg: TaskContract):
    print(f"Received task\n:id {msg.id}\n topic: {msg.topic} \nregion: \n{msg.region}")
