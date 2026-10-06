from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import update
from database import get_db
import models
from squemas import dogResponse, dog
from typing import List

router = APIRouter(

    prefix="/dogs",
    tags=["dogs"],
)


@router.get("/", response_model=List[dogResponse])
def get_dogs(db: Session = Depends(get_db)):
    dogs = db.query(models.dogs).all()
    if not dogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No hay perritos :c")
    return dogs

@router.post("/", response_model=dogResponse)
def create_dog(dog: dog, db: Session = Depends(get_db)):
    db_dog = models.dogs(
        name=dog.get_name(),
        gender=dog.get_gender(),
        power=dog.power,
        won_battles=dog.won_battles,
        health=dog.health
    )
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

@router.get("/restore")
def restaurar_health(db: Session = Depends(get_db)):
    db.execute(
        update(models.dogs).values(health=100)
    )
    db.commit()

    return 0

@router.get("/{id}", response_model=dogResponse)
def get_dog(id: int, db: Session = Depends(get_db)):

    query_buscar_perro = db.query(models.dogs).filter(models.dogs.id == id)
    perro = query_buscar_perro.first()

    if perro is None:
        raise HTTPException(status_code=404, detail="este perro no existe")

    return perro