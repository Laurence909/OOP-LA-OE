#LA9
class Car:
    def __init__(self, brand):
        self.brand = brand
        
    def __str__(self):
        return f"Car brand: {self.brand}"

car1 = Car("TOYOTA")
print(car1)
del(car1)
print(car1)
