from database import SessionLocal, engine
from models import dogs
from squemas import dog

db = SessionLocal()

perro1 = dog(name="Leo", gender="male")

dogs_database = dogs(
    name=perro1.get_name(),
    gender=perro1.get_gender(),
    power=perro1.power,
    won_battles=perro1.won_battles,
    health=perro1.health
)

db.add(dogs_database)
db.commit()
db.refresh(dogs_database)

print(dogs_database.id)
