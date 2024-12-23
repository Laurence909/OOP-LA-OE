#LA11
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
    def describePhone(self):
        print(f"Brand: {self.brand} and the model is: {self.model}")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)
samsung = Android("samsung", "SUPER ULTRA MEGA EVOLVED")
samsung.describePhone()
