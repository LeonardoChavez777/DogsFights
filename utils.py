import random

from models import dogs
import time

#creo q esto se borra:
from database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends

def pelea(perro1: dogs, perro2: dogs, db):
    presentar(perro1, perro2)
    hacer_la_cuenta()

    for i in range(3):
        time.sleep(2)
        print(f"\n================== Ronda {i + 1} ==================")

        time.sleep(2)
        ataque(perro1,perro2,db)
        resultado_perr2 = revisar_muerte(perro2)
        if resultado_perr2[1]:
            #perro2murio
            print(f"{perro1.name} ha matado a {perro2.name}!!!")
            aumentar_cuenta_ganadora(perro1,perro2,db)
            return perro1
        time.sleep(3)
        ataque(perro2,perro1,db)
        resultado_perr1 = revisar_muerte(perro1)
        if resultado_perr1[1]:
            #perro1 ha muerto!
            print(f"{perro2.name} ha matado a {perro1.name}!!!")
            aumentar_cuenta_ganadora(perro2,perro1,db)
            return perro2

        time.sleep(2)
        print(f"\n------- Resultados de la ronda {i + 1} -------")
        time.sleep(2)
        print(resultado_perr1[0])
        time.sleep(2)
        print(resultado_perr2[0])

    ganador, perdedor = comparar_salud(perro1, perro2)
    aumentar_cuenta_ganadora(ganador, perdedor,db)
    present_winner(ganador)

    return ganador  



def presentar(perr1: dogs, perr2: dogs):
    print(f"¡Bienvenidos a la pelea entre {perr1.name} y {perr2.name}!")
    time.sleep(2)
    print(f"{perr1.name} tiene {perr1.health} puntos de salud y un poder de {perr1.power}.")
    time.sleep(2)
    print(f"{perr2.name} tiene {perr2.health} puntos de salud y un poder de {perr2.power}.")
    time.sleep(2)

def comparar_salud(dog1: dogs, dog2: dogs):
    if dog1.health > dog2.health:
        return dog1, dog2
    elif dog2.health > dog1.health:
        return dog2, dog1
    else:
        return None  # empate

def revisar_muerte(dog: dogs):
    if dog.health <= 0:
        result = (f"{dog.name} ha sido asesinado!")
        #matar al perro en la base de datos
        return result, True
    else:
        result = (f"{dog.name} tiene {dog.health} puntos de salud restantes.")
        return result, False

def ataque(perro1: dogs, perro2: dogs, db):
    daño = perro1.power * random.uniform(0.5, 1)
    daño = round(daño)
    perro2.health = perro2.health - daño
    print(f"{perro1.name} le ha hecho {daño} de daño a {perro2.name}")
    db.commit()
    db.refresh(perro2)

def hacer_la_cuenta():
    time.sleep(2)
    for i in range(4):
        if i == 3:
            print("***************** ¡Comienza la pelea! *****************")
        else:
            print(3 - i)
            time.sleep(1)

def present_winner(perroganador: dogs):
    if perroganador is None:
        print("¡La pelea terminó en empate!")
    else:
        print(f"¡El ganador es {perroganador.name} con {perroganador.health} puntos de salud restantes y un poder de {perroganador.power}!")

def aumentar_cuenta_ganadora(perroganador: dogs, perroperdedor: dogs, db):
    perroganador.won_battles += 1
    perroganador.power = perroganador.power + round(perroperdedor.power * 0.2)
    db.commit()
    db.refresh(perroganador)

    