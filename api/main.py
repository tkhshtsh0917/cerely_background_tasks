from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

from background.task import executor, calc_bmi


class Body(BaseModel):
    weight: float
    height: float


class TaskStatus(BaseModel):
    id: str
    status: str
    result: Optional[str]


app = FastAPI()


@app.post('/bmi', response_model=TaskStatus, response_model_exclude_unset=True)
def calculate_bmi(body: Body):
    task = calc_bmi.delay(weight=body.weight, height=body.height)
    return TaskStatus(id=task.id, status="PENDING", result=None)


@app.get('/bmi/{task_id}', response_model=TaskStatus)
def check_status(task_id: str):
    result = executor.AsyncResult(task_id)

    return TaskStatus(
        id=task_id,
        status=result.status,
        result=str(result.result),
    )
