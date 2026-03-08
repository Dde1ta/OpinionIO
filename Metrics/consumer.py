from General.kafkaContracts import ResearchMetrics
from General.kafkaHelper import kafka_app
from General.logger import Logger
from .logic import write_metric_to_db # Updated import

logger = Logger(name="Metrics.Consumer")

@kafka_app.consumes(topic="SAVE_METRICS",
                    group_id="metrics_worker_group")
async def write_metric(msg: ResearchMetrics):
    logger.info(f"[KAFKA] Received metric | id={msg.id} process={msg.process}")
    await write_metric_to_db(msg) # Updated function call