from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.consumes(topic="COMPLETED_INFLUENTIAL_TASK")
async def get_influential_result(msg: CompletedInfluentialTaskContract) -> CompletedInfluentialTaskContract:
    return msg


@kafka_app.consumes(topic="COMPLETED_BULK_TASK")
async def get_bulk_result(msg: CompletedBulkTaskContract) -> CompletedBulkTaskContract:
    return msg
