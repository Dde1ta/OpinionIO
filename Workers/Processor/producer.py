from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.produces(topic="TASK_DATA")
async def push_task_data(task_data: TaskDataContract) -> TaskDataContract:
    return task_data
