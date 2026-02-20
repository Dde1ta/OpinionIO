from Apis.general.kafkaHelper import *
from .contracts import *


@kafka_app.consumes(topic="NEW_TASK")
async def test(msg: TaskContract):
    print(f"Received task\n:id {msg.id}\n topic: {msg.topic} \nregion: \n{msg.region}")
