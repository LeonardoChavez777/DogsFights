from utils import pelea
from models import dogs
import time

#en el endpoint comprobar q el numero de perros sea una potencia de dos
def torneo(perros: list[dogs], db):

    while len(perros)>1:
        ganadores = []

        for i in range(0, len(perros), 2):
            ganador = pelea(perros[i],perros[i+1],db)
            ganadores.append(ganador)
            if len(perros) == 2:
                print(f"\n\n{ganador.name} ha Ganado el torneo!!!\n\n")
                ganador.health = 100
            else:
                print(f"\n\n{ganador.name} ha pasado a la siguiente ronda!!!\n\n")
                time.sleep(3)
                ganador.health = ganador.health + 20

        perros = ganadores

    return perros[0]