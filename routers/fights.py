from fastapi import APIRouter, Depends, HTTPException
import squemas
from sqlalchemy.orm import Session
from database import get_db
import models
from utils import pelea
from torneo import torneo
from tasks.peleas import pelea_de_perros, torneo_de_perros


router = APIRouter(
    prefix="/fights",
    tags=["fights"]
)

@router.post("/", response_model=squemas.dog)
def dog_fight(id_dog1: int, id_dog2: int, db: Session = Depends(get_db)):

    database_perro1 = db.get(models.dogs,id_dog1)
    database_perro2 = db.get(models.dogs,id_dog2)

    if(database_perro1.health <= 0 or database_perro2.heatlh <=0):
         raise HTTPException(
             status_code=400,
             detail="Los muertos no pelean"
         )

    ganador = pelea(database_perro1, database_perro2, db)

    return ganador

@router.post("/async")
def dog_fight_async(id_dog1: int, id_dog2:int, db: Session = Depends(get_db)):


    database_perro1 = db.get(models.dogs,id_dog1)
    database_perro2 = db.get(models.dogs,id_dog2)
    
    if(database_perro1.health <= 0 or database_perro2.health <=0):
             raise HTTPException(
                 status_code=400,
                 detail="Los muertos no pelean"
             )

    task = pelea_de_perros.delay(id_dog1,id_dog2)

    return {"pelea_id": task.id}


@router.post("/torneo")
def torneo_perros_4(p1: int, p2: int, p3: int, p4: int, db: Session = Depends(get_db)):

    perros = []

    database_perro1 = db.get(models.dogs,p1)
    database_perro2 = db.get(models.dogs,p2)
    database_perro3 = db.get(models.dogs,p3)
    database_perro4 = db.get(models.dogs,p4)

    if(database_perro1.health <= 0 or database_perro2.health <=0 or database_perro3.health <=0 or database_perro4.health <=0):
             raise HTTPException(
                 status_code=400,
                 detail="Los muertos no pelean"
             )

    perros.append(database_perro1)
    perros.append(database_perro2)
    perros.append(database_perro3)
    perros.append(database_perro4)

    ganador = torneo(perros=perros,db=db)

    return ganador

@router.post("/torneo/async")
def torneo_perros_4_async(p1: int, p2: int, p3: int, p4: int, db: Session = Depends(get_db)):

    database_perro1 = db.get(models.dogs,p1)
    database_perro2 = db.get(models.dogs,p2)
    database_perro3 = db.get(models.dogs,p3)
    database_perro4 = db.get(models.dogs,p4)

    if(database_perro1.health <= 0 or database_perro2.health <=0 or database_perro3.health <=0 or database_perro4.health <=0):
             raise HTTPException(
                 status_code=400,
                 detail="Los muertos no pelean"
             )

    task = torneo_de_perros.delay(p1,p2,p3,p4)

    return {"torneo_id": task.id}
    
      
            