from General.kafkaContracts import *
from General.kafkaHelper import kafka_app


@kafka_app.produces(topic="META_DATA")
async def push_meta_data(meta_data: MetaDataContract) -> MetaDataContract:
    return meta_data



