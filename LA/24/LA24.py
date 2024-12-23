#LA24
from abc import ABC, abstractmethod

class GameCharacter(ABC):
    @abstractmethod
    def attack(self):
        pass
    
class Warrior(GameCharacter):
    def attack(self):
        print("Warrior: SUNTUKIN MO!")
        
class Mage(GameCharacter):
    def attack(self):
        print("Mage: Casts a punch!")
        
class Archer(GameCharacter):
    def attack(self):
        print("Archer: sapul ka nanaman!")
        
class Healer(GameCharacter):
    def attack(self):
        print("Healer: Revive me jett!")
        
suntok = Warrior()
cast = Mage()
sapul = Archer()
revive = Healer()
suntok.attack()
cast.attack()
sapul.attack()
revive.attack()
