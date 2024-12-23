#LA17
import random

class Player:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def attack(self, target):
        target.hp -= self.attack_power
        if target.hp < 0:
            target.hp = 0

        print(f"{self.name} attacks! It deals {self.attack_power} damage and reduces {target.name}'s HP to {target.hp}")

    def heal(self, heal_amount):
        self.hp += heal_amount
        print(f"{self.name} heals for {heal_amount} HP! Current HP is {self.hp}")

Jobert = Player("Jobert", 10000, 2000)
Kumunoy = Player("Kumunoy", 20000, 3000)

characters = [Jobert, Kumunoy]


while all(character.hp > 0 for character in characters):
    if random.choice([True, False]):
        Jobert.attack(Kumunoy)
    else:
        Jobert.heal(200)


    if Kumunoy.hp > 0:
        if random.choice([True, False]):
            Kumunoy.attack(Jobert)
        else:
            Kumunoy.heal(300)

if Jobert.hp > Kumunoy.hp:
    print(f"{Jobert.name} wins the battle!")
elif Kumunoy.hp > Jobert.hp:
    print(f"{Kumunoy.name} wins the battle!")
else:
    print("It's a tie!")

print("GAME OVER!")
