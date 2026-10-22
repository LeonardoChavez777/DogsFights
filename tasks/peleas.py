from core.celery_app import celery_app
import torneo
from utils import pelea
import models
from database import SessionLocal


@celery_app.task
def pelea_de_perros(id1, id2):
    db = SessionLocal()
    try:
        p1 = db.query(models.dogs).filter(models.dogs.id == id1).first()
        p2 = db.query(models.dogs).filter(models.dogs.id == id2).first()

        ganador = pelea(p1,p2,db)

        return ganador.name

    finally:
        db.close()


@celery_app.task
def torneo_de_perros(id1, id2, id3, id4):
    db = SessionLocal()
    try:
        p1 = db.query(models.dogs).filter(models.dogs.id == id1).first()
        p2 = db.query(models.dogs).filter(models.dogs.id == id2).first()
        p3 = db.query(models.dogs).filter(models.dogs.id == id3).first()
        p4 = db.query(models.dogs).filter(models.dogs.id == id4).first()

        perros = [p1, p2, p3, p4]

        ganador = torneo.torneo(perros,db)

        return ganador.name

    finally:
        db.close()