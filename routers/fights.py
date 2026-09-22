from fastapi import APIRouter, Depends
import squemas
from sqlalchemy.orm import Session
from database import get_db
import models
import peleas
from utils import pelea

import database
router = APIRouter(
    prefix="/fights",
    tags=["fights"]
)

@router.post("/", response_model=squemas.dog)
def dog_fight(id_dog1: int, id_dog2: int, db: Session = Depends(get_db)):

    database_perro1 = db.get(models.dogs,id_dog1)
    database_perro2 = db.get(models.dogs,id_dog2)

    ganador = pelea(database_perro1, database_perro2, db)

    return ganador


    