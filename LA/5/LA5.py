#LA5
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} is a {self.role} hero."


Gojo = Hero("Gojo", "Mage")
print(Gojo.describe())
