#LA18
class Lumpia:
    def __init__(self, lumpia, sahog1, sahog2, sahog3, sahog4):
        self.__lumpia = lumpia
        self.__sahog1 = sahog1
        self.__sahog2 = sahog2
        self.__sahog3 = sahog3
        self.__sahog4 = sahog4

    def __str__(self): 
        return f"Meat: {self.__lumpia}\n1st Ingridient: {self.__sahog1}\n2nd Ingridient: {self.__sahog2}\n3rd Ingridient: {self.__sahog3}\n4th Ingridient: {self.__sahog4}\n"

    
Shanghai = Lumpia("Giniling (Pork)", "carrot", "sibuyas", "Lumpia Wrapper", "seasonings")
Lumpiang_Toge = Lumpia("Giniling (Pork)", "Toge", "Tokwa", "Lumpia Wrapper", "seasonings")
Lumpiang_Sariwa = Lumpia("small shrimp", "carrot", "lettuce", "Tokwa", "green beans")


print("Shanghai")
print(Shanghai)

print("Lumpiang Toge")
print(Lumpiang_Toge)

print("Lumpiang Sariwa")
print(Lumpiang_Sariwa)
