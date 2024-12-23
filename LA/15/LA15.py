#LA15
class DOG:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Bark!")
class CAT:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Meow!")
class BIRD:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Chirp!")
class FISH:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: ...")


dog = DOG("teban") 
cat = CAT("gwen")
bird = BIRD("kurimaw")
fish = FISH("igado")


for animal in [dog, cat, bird, fish]:
    animal.speak()
