from celery import Celery

celery_app = Celery(
    "celery_app",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
    include=[
        "tasks.peleas"
    ]
)

celery_app.conf.update(
    task_track_started=True,
    result_expires=3600
)