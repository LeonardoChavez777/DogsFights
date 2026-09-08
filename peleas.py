import perro
import time


class Fight:
    def __init__(self, dog1, dog2):
        self.dog1 = dog1
        self.dog2 = dog2

    def present_fighters(self):
        print(f"¡Bienvenidos a la pelea entre {self.dog1.get_name()} y {self.dog2.get_name()}!")
        time.sleep(2)
        print(f"{self.dog1.get_name()} tiene {self.dog1.health} puntos de salud y un poder de {self.dog1.power}.")
        time.sleep(2)
        print(f"{self.dog2.get_name()} tiene {self.dog2.health} puntos de salud y un poder de {self.dog2.power}.")
        time.sleep(2)

    def present_winner(self, winner):
        if winner is None:
            print("¡La pelea terminó en empate!")
        else:
            print(f"¡El ganador es {winner.get_name()} con {winner.health} puntos de salud restantes y un poder de {winner.power}!")

    def start_fight(self):
        self.present_fighters()
        result = fight(self.dog1, self.dog2)
        self.present_winner(result)
        return result

def compare_health(dog1, dog2):
    if dog1.health > dog2.health:
        return dog1
    elif dog2.health > dog1.health:
        return dog2
    else:
        return None  # It's a tie

def revisar_muerte(dog1):
    if dog1.health <= 0:
        result = (f"{dog1.get_name()} ha sido asesinado!")
        dog1.dog_dead()
        return result, True
    else:
        result = (f"{dog1.get_name()} tiene {dog1.health} puntos de salud restantes.")
        return result, False

def fight(dog1, dog2):
    # esperar tres segundos antes de continuar
    time.sleep(2)

    for i in range(4):
        if i == 3:
            print("***************** ¡Comienza la pelea! *****************")
        else:
            print(3 - i)
            time.sleep(1)

    time.sleep(2)  # Wait for 2 seconds before the fight starts

    for i in range(3):  # 3 rounds of fighting
        time.sleep(2)
        print(f"\n================== Ronda {i + 1} ==================")

        time.sleep(2)  # Wait for 2 seconds before the round starts
        dog1.attack(dog2)

        resultado_round_dog1 = revisar_muerte(dog2)
        if resultado_round_dog1[1]:  # Check if dog2 is dead
            dog1.battle_won(dog2)
            return dog1

        time.sleep(3)
        dog2.attack(dog1)
        
        resultado_round_dog2 = revisar_muerte(dog1)
        if resultado_round_dog2[1]:  # Check if dog1 is dead
            dog2.battle_won(dog1)
            return dog2

        time.sleep(2)
        print(f"\n------- Resultados de la ronda {i + 1} -------")        
        time.sleep(2)
        print(resultado_round_dog1[0])
        time.sleep(2)
        print(resultado_round_dog2[0])


    ganador = compare_health(dog1, dog2)
    ganador.battle_won(dog1 if ganador == dog2 else dog2)
    time.sleep(2)
    print("\n***************** La pelea ha terminado *****************")
    

    return ganador



