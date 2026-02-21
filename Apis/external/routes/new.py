from fastapi import APIRouter, Depends
from General.database import *
from ..kafka_helper.producers import *
from General.kafkaContracts import *
from ..models import Task

new_router = APIRouter(
    prefix="/api/external/new"
)


@new_router.post("/")
async def new(task: Task, db: AsyncSession = Depends(get_db)):
    try:
        contract = TaskContract(**task.model_dump())
        await new_task(contract)

        status = TaskStatus(
            id=task.id,
            status="queued",
        )

        db.add(status)
        await db.commit()

        return {"status": "queued", "id": task.id}

    except Exception as e:
        return {"status": "Failed", "message": e}
