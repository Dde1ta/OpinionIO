from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.consumes(topic="TASK_DATA")
async def next_task(msg: TaskDataContract) -> TaskDataContract:
    return msg
