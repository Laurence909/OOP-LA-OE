#LA12
class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
    def describeToy(self):
        print(f"Toy: {self.name}\nPrice is: {self.price}")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)
car = Car("car", "2500")
car.describeToy()
