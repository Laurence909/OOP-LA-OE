#LA16
class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def operate(self):
        print("OPERATING")
    def info(self):
        print(f"Brand: {self.brand} Model: {self.model}")
        
class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")
class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")
class Microwave(Appliance):
    def operate(self):
        print("Heating food!")

samsung = WashingMachine("samsung", "kurkur")
KAWA = Refrigerator("Kawa", "wa")
pinoy = Refrigerator("pinoy", "ako")

for ap in [samsung, KAWA, pinoy]:
    ap.operate()
    ap.info()
