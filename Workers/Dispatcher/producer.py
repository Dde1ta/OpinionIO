from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.produces(topic="INFLUENTIAL_TASK")
async def queue_tiny_bert(influential_task: InfluentialTaskContract) -> InfluentialTaskContract:
    return influential_task


@kafka_app.produces(topic="BULK_TASK")
async def queue_xg_boost(bulk_task: BulkTaskContract) -> BulkTaskContract:
    return bulk_task
