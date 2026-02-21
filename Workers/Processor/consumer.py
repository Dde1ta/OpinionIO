from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.consumes(topic="META_DATA")
async def next_task(msg: MetaDataContract) -> MetaDataContract:
    return msg
