#LA13

class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        
    def describeAnimal(self):
        print(f"animal: {self.name}\ntype is: {self.type}\n")

class Fish(Animal):
    def __init__(self, name, type, can_swim):
        super().__init__(name, type)
        self.can_swim = can_swim
        
goldfish = Fish("goldfish", "fish", True)

goldfish.describeAnimal()
print(goldfish.can_swim)
