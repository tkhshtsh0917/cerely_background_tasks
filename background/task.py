import os
import time

from celery import Celery  # type: ignore


executor = Celery(__name__)

executor.conf.broker_url = os.environ.get(
    "CELERY_BROKER_URL", "redis://broker:6379/0"
)
executor.conf.result_backend = os.environ.get(
    "CELERY_BACKEND_URL", "redis://broker:6379/1"
)


@executor.task(name="tasks.calc_bmi")
def calc_bmi(weight: float, height: float) -> float:
    time.sleep(10)
    return weight / height**2
