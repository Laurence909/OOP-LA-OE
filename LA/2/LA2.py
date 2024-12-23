#LA2
class ml_hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

hero1 = ml_hero("Hayabusa", "Assassin")

print(f"Name = {hero1.name}\nRole = {hero1.role}\n")
print(f"{hero1.name} is a {hero1.role}")
