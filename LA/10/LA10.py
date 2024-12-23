#LA10
class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle (self):
        print(f"Brand: {self.brand} \nhas a model: {self.model} \nfuel_type: {self.fuel_type}\n")

class Car(Vehicle):
    pass
class Motor(Vehicle):
    pass

lambo = Car ("lambo", "model lang", "gas")
lambo.describeVehicle()
mio = Motor("mio", "yobmot", "100 gas")
mio.describeVehicle()
