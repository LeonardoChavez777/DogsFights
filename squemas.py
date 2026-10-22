import random
from pydantic import BaseModel, Field
class dog(BaseModel):

    name: str
    gender: str
    power: int = Field(default_factory=lambda: random.randint(1, 30))
    won_battles: int = 0
    health: int = 100

    def ladrar(self):
        return f"{self.name} está ladrando."

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def reproduce(self, partner):
        if self.gender != partner.get_gender():
            # Create a new dog instance with a name based on the parents' names
            new_name = f"{self.name}-{partner.get_name()}"

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
        self.name = new_name

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

class dogResponse(BaseModel):
    id: int
    name: str
    gender: str
    power: int
    won_battles: int
    health: int

    model_config = {
        "from_attributes": True
    }