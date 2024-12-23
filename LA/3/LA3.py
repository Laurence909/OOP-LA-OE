#LA3
class ml_hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def heroObject(self):
        return f"{self.name} is {self.role} hero."
    
    def __str__(self):
        return f"{self.name} is {self.role} hero."

        

hero1 = ml_hero("Gojo", "Mage")
hero2 = ml_hero("Hayabusa", "Assassin")

print(f"Name: {hero1.name} \nRole: {hero1.role}")
print(ml_hero.heroObject(hero1))
print(hero1)
print()
print(f"Name: {hero2.name} \nRole: {hero2.role}")
print(ml_hero.heroObject(hero2))
print(hero2)
