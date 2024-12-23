#OE1
class Hero:
    def __init__(self,name,role,damage_type):
        self.name = name
        self.role = role
        self.damage_type = damage_type

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, Damage: {self.damage_type}"

    def team_description(self):
        return f"{self.name} plays the role of {self.role} and deals {self.damage_type} damage"

Yu_Zhong = Hero("Yu Zhong", "Exp", "Attack")
Xavier = Hero("Xavier", "Mid", "Magic")
Hayabusa = Hero("Hayabusa", "Jungle", "Attack")
Beatrix = Hero("Beatrix", "Marksman", "Attack")
Franco = Hero("Franco", "Tank", "Attack")

heroes=[Yu_Zhong,Xavier,Hayabusa,Beatrix,Franco]

print("My team:")
for hero in heroes:
    print(hero)
    
print()

print("Team description:")
for hero in heroes:
    print(hero.team_description())
