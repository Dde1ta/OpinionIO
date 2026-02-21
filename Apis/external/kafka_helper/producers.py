from .contracts import *
from General.kafkaHelper import kafka_app


@kafka_app.produces(topic="NEW_TASK")
async def new_task(task: TaskContract):
    return task
