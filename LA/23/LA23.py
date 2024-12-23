#LA23
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, function_name):
        def initial_function(*args, **kwargs):
            print("Introducing......")
            function_name(*args, **kwargs)
            print("This character is Amazing!")
        return initial_function
        
Ichigo = AnimeCharacter("Ichigo", "Getsuga tensho")

@Ichigo.introduce
def character_intro():
    print(f"{Ichigo.name}! use {Ichigo.ability}!")
character_intro()
