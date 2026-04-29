from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # <-- Add this import
from contextlib import asynccontextmanager
from General.kafkaHelper import kafka_app
from General.logger import Logger
from General.config import settings
from General.database import init_db
from .routes.new import *
from .routes.status import *
from .kafka_helper import producers
from .kafka_helper import consumers

logger = Logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with kafka_app.fastapi_lifespan(kafka_broker_name=settings.environment)(app):
        logger.info("Producer Created at External")
        await init_db()
        logger.info("DB Connected")
        yield
        logger.info("Producer Flushed and FastKafka Shut Down")

external = FastAPI(lifespan=lifespan)

# --- ADD THIS CORS BLOCK ---
external.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace "*" with your React app's URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ---------------------------

external.include_router(new_router)
external.include_router(status_router)
