#OE4
import random

class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, target):
        target.hp -= self.power
        print(f"{self.name} attacked {target.name}, dealing {self.power} damage!")

    def special_move(self):
        print(f"{self.name} prepares to unleash a special move!")


class Warrior(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.rage_mode = False

    def special_move(self, target):
        if self.rage_mode:
            target.hp -= self.power
            print(f"{self.name} enters Rage Mode again, smashing {target.name} for {self.power} damage!")
            self.power //= 2
            self.rage_mode = False
        else:
            self.power *= 2
            print(f"{self.name} activates Rage Mode, doubling their power!")
            self.attack(target)
            self.rage_mode = True

    def defend(self, attacker):
        reduced_damage = attacker.power // 2
        self.hp -= reduced_damage
        print(f"{self.name} blocks, reducing damage taken from {attacker.name} to {reduced_damage}.")


class Mage(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def special_move(self, target):
        print(f"{self.name} casts Arcane Blast, dealing {self.power} magical damage to {target.name}!")
        target.hp -= self.power

    def defend(self, attacker):
        reduced_damage = attacker.power // 3
        self.hp -= reduced_damage
        print(f"{self.name} conjures a shield, reducing damage from {attacker.name} to {reduced_damage}.")


class Archer(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def special_move(self, target):
        print(f"{self.name} fires a Rain of Arrows, striking {target.name} for {self.power} damage!")
        target.hp -= self.power

    def defend(self, attacker):
        reduced_damage = attacker.power // 4
        self.hp -= reduced_damage
        print(f"{self.name} dodges, reducing damage taken from {attacker.name} to {reduced_damage}.")


class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)

    def special_move(self):
        heal_amount = random.randint(100, 300)
        self.hp += heal_amount
        print(f"{self.name} roars furiously, restoring {heal_amount} health!")


freya = Warrior("Freya", 5000, 1000)
lou_yi = Mage("Lou Yi", 3000, 1500)
miya = Archer("Miya", 2500, 2500)
turtle = Monster("Turtle", 8000, 1200)

heroes = [freya, lou_yi, miya]

for hero in heroes:
    print(f"{hero.name}:\nHp: {hero.hp}\nAttack: {hero.power}\n")

while len(heroes) > 0 and turtle.hp > 0:
   
    attacker = random.choice(heroes)
    attacker.special_move(turtle)
    print(f"{turtle.name}'s current HP: {turtle.hp}\n")

    if turtle.hp <= 0:
        print(f"{turtle.name} has been defeated by the heroes!")
        break

    
    turtle.attack(attacker)
    print(f"{attacker.name}'s current HP: {attacker.hp}\n")

    if attacker.hp > 0:
        attacker.defend(turtle)
    else:
        attacker.hp = 0
        print(f"{attacker.name} has fallen in battle!\n")
        heroes.remove(attacker)

    
    if turtle.hp > 0 and random.choice([True, False]):
        turtle.special_move()
        print(f"{turtle.name}'s current HP: {turtle.hp}\n")

print("\nGAME OVER!")
if not heroes:
    print("The Turtle has vanquished the heroes!")
elif turtle.hp <= 0:
    print("The heroes have triumphed over the Turtle!")
