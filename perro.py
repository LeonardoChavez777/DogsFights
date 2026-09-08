import random

class dog():
    def __init__(self, name, gender, power=None, won_battles=0, health=100):
        self.nombre = name
        self.genero = gender
        self.won_battles = won_battles
        self.health = health
        if power is not None:
            self.power = power
        else:   
            #establece un atributo de poder para el perro random
            self.power = random.randint(1, 20)

    def ladrar(self):
        return f"{self.nombre} está ladrando."

    def get_name(self):
        return self.nombre

    def get_gender(self):
        return self.genero

    def reproduce(self, partner):
        if self.genero != partner.get_gender():
            # Create a new dog instance with a name based on the parents' names
            new_name = f"{self.nombre}-{partner.get_name()}"

            # se asigna un genero aleatorio al nuevo perro
            new_gender = random.choice(['male', 'female'])
            # si es female el poder se reduce un 20 porciento
            if new_gender == "female":
                new_power = (self.power + partner.power) / 2 * 0.8 + random.randint(-10, +10)  # Average power of the parents with some variation
            else:
                new_power = (self.power + partner.power) / 2 + random.randint(-10, +10)  # Average power of the parents with some variation

            print(f"Se ha creado un nuevo perro: {new_name}, Género: {new_gender}, Poder: {new_power}")

            return dog(name=new_name, gender=new_gender, power=new_power)
        else:
            raise ValueError("Los perros deben ser de géneros opuestos para reproducirse.")

    def name_dog(self, new_name):
        self.nombre = new_name

    def battle_won(self, opponent):
        self.won_battles += 1
        self.power = self.power + 5 + round(opponent.power * 0.1) # Increase power by 1 for each battle won

    def hurt(self, amount):
        self.health -= amount

    def attack(self, opponent):
        # Calculate damage based on power and a random factor
        damage = self.power * random.uniform(0.5, 1)
        damage = round(damage)
        opponent.hurt(damage)
        print(f"{self.get_name()} inflige {damage} puntos de daño a {opponent.get_name()}")

    def dog_dead(self):
        del self