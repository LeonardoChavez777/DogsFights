import time
from peleas import Fight
import perro

Leo = perro.dog(name="Leo", gender="male")
Vicky = perro.dog(name="Vicky", gender="female")

Fight1 = Fight(Leo, Vicky)
Fight1.start_fight()