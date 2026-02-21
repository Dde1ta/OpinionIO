from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.consumes(topic="NEW_TASK")
async def next_task(msg: TaskContract) -> TaskContract:
    return msg