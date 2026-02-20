from fastapi import FastAPI
from contextlib import asynccontextmanager
from Apis.general.logger import Logger
from Apis.general.database import init_db
from .kafka_helper.producers import *
from .kafka_helper.consumers import *
from .routes.new import *
from .routes.status import *
from .kafka_helper.contracts import *
from Apis.general.kafkaHelper import *

logger = Logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with kafka_app.fastapi_lifespan(kafka_broker_name="localhost")(app):
        logger.info("Producer Created at External")

        # 2. Run your other custom startup logic
        await init_db()
        logger.info("DB Connected")

        # 3. Yield control to the FastAPI application
        yield

        # FastKafka will automatically handle flushing and shutting down
        # its producers/consumers when the code exits the 'async with' block!
        logger.info("Producer Flushed and FastKafka Shut Down")


external = FastAPI(lifespan=lifespan)

external.include_router(new_router)
