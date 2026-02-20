from pydantic import BaseModel

# models


class Task(BaseModel):
    id: int
    topic: str
    region: str
