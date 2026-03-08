from sqlalchemy import Column, Integer, String, delete
from sqlalchemy.future import select
from General.logger import Logger
from General.kafkaContracts import ResearchMetrics
from General.database import ResearchMetricDB   , AsyncSessionLocal

logger = Logger(name="Metrics.Logic")


# ── 2. Database Operations ───────────────────────────────────────────────────
async def write_metric_to_db(metric: ResearchMetrics):
    """Save a single ResearchMetrics record to the database."""
    async with AsyncSessionLocal() as session:
        new_metric = ResearchMetricDB(
            id=str(metric.id),
            process=metric.process,
            start_time=str(metric.start_time),
            end_time=str(metric.end_time),
            total_time=str(metric.total_time)
        )
        session.add(new_metric)
        await session.commit()

    logger.info(f"[DB] Written metric | id={metric.id} process={metric.process} total_time={metric.total_time}ms")


async def read_all_metrics() -> list[dict]:
    """Read every row from the DB and return as a list of dicts to match old CSV behavior."""
    async with AsyncSessionLocal() as session:
        result = await session.execute(select(ResearchMetricDB))
        records = result.scalars().all()

        # Format it exactly how the old CSV DictReader did
        return [
            {
                "id": r.id,
                "process": r.process,
                "start_time": r.start_time,
                "end_time": r.end_time,
                "total_time": r.total_time,
            }
            for r in records
        ]


async def clear_metrics():
    """Wipe the table for the next experiment run."""
    async with AsyncSessionLocal() as session:
        await session.execute(delete(ResearchMetricDB))
        await session.commit()
    logger.info("[DB] Cleared all metrics")

