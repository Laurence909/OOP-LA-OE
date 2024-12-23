#LA14
class Spiderman():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def describSpiderman(self):
        print(f"Name: {self.name}\n{self.age}")
class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
    def printInfo(self):
        print(f"Name: {self.name.upper()}\nMovie Title: {self.movieTitle}")
        
class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
    def printInfo(self):
        print(f"Name: {self.name.upper()}\nMovie Title: {self.movieTitle}")
        
class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle
        
    def printInfo(self):
        print(f"Name: {self.name.upper()}\nMovie Title: {self.movieTitle}")
        
tobey = Tobey("tobey", 40, "spyderman")
andrew = Andrew("andrew", 30, "spyderman")
tom = Tom("tom", 20, "spyderman")

tobey.printInfo()
andrew.printInfo()
tom.printInfo()
