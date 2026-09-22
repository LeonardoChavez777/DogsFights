from core.celery_app import celery_app
from utils import pelea
from models import dogs
@celery_app.task
def pelea_de_perros(p1: dogs, p2: dogs, db):
    ganador = pelea(p1,p2,db)
    return ganador
