from fastapi import APIRouter, Depends, HTTPException
from General.database import *
from General.kafkaContracts import *
from Apis.internal.Result_handler.filter_results import filter_result

results_router = APIRouter(
    prefix="api/internal/results"
)


@results_router.post("/influential")
async def submit_influential_result(result: CompletedInfluentialTaskContract, db: AsyncSession = Depends(get_db)):
    try:
        filtered = filter_result(result)

        to_insert = InfluentialResults(
            id=filtered.id,
            most_positive=filtered.most_positive,
            most_negative=filtered.most_negative,
            mode_sentiment=filtered.modal_sentiment)

        db.add(to_insert)

        await db.commit()

        return {"status": "Success"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insert failed: {str(e)}")


@results_router.post("/bulk")
async def submit_bulk_result(result: CompletedBulkTaskContract, db: AsyncSession = Depends(get_db)):
    try:
        filtered = filter_result(result)

        to_insert = BulkResults(
            id=filtered.id,
            most_positive=filtered.most_positive,
            most_negative=filtered.most_negative,
            mode_sentiment=filtered.modal_sentiment)

        db.add(to_insert)

        await db.commit()

        return {"status": "Success"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database insert failed: {str(e)}")
