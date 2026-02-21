from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.consumes(topic="INFLUENTIAL_TASK")
async def next_task(msg: InfluentialTaskContract) -> InfluentialTaskContract:
    return msg


@kafka_app.consumes(topic="BULK_TASK")
async def next_task(msg: BulkTaskContract) -> BulkTaskContract:
    return msg
