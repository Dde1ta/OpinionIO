from fastapi import APIRouter, Depends, HTTPException
from General.database import *
from General.kafkaContracts import *
from Apis.internal.Result_handler.filter_results import filter_result

status_router = APIRouter(
    prefix="/api/internal/status"
)


@status_router.post('/{task_id}')
async def set_status(task_id: int, status: str, db: AsyncSession = Depends(get_db)):
    try:
        # Use async db.get() for SQLAlchemy async sessions
        task = await db.get(TaskStatus, task_id)
        
        if not task:
            raise HTTPException(404, f"Task with id {task_id} not found")

        task.status = status

        await db.commit()

        return {"status": "updated", "task_id": task_id, "updated_status": status}

    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        raise HTTPException(500, f"Failed to set status: {str(e)}")
