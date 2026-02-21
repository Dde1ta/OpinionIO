from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.produces(topic="COMPLETED_INFLUENTIAL_TASK")
async def submit_result_tiny_bert(results: CompletedInfluentialTaskContract) -> CompletedInfluentialTaskContract:
    return results


@kafka_app.produces(topic="COMPLETED_BULK_TASK")
async def submit_result_tiny_bert(results: CompletedBulkTaskContract) -> CompletedBulkTaskContract:
    return results
