from celery import Celery
from celery.schedules import crontab

celery_app = Celery(
    "worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

celery_app.autodiscover_tasks(["app"])

celery_app.conf.beat_schedule = {
    "send-message-every-10-seconds": {
        "task": "app.tasks.send_message",
        "schedule": 30.0,  # seconds
    },
}

celery_app.conf.timezone = "UTC"
