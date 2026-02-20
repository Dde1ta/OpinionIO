from Apis.general.kafkaHelper import *
from .contracts import *


@kafka_app.produces(topic="NEW_TASK")
async def new_task(task: TaskContract):
    return task
