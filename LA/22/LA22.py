#LA22
class parties:
    def __init__(self, party_theme, list_of_foods, secret):
        self.party_theme = party_theme
        self.list_of_foods = list_of_foods
        self.secret = secret
    def __secret(self):
        print(f"ang secret dish ay {self.secret}")
    def foods(self):
        print(f"\nTheme: {self.party_theme}\nlist_of_foods: {self.list_of_foods}")
        self.__secret()
        
xmas_party = parties("xmas_party", "lumpia, spag, sinigang na pusit, hotdog, graham", "menudo")
year_end_party = parties("year_end_party", "lumpia, puto, grapes", "lechon")
holloween_party = parties("holloween_party", "candies, chocolate", "cake")

xmas_party.foods()
year_end_party.foods()
holloween_party.foods()


class Regalo:
    def __init__(self, laman, wrapper):
        self.__laman = laman
        self.wrapper = wrapper
    def buksan(self, function_name):
        def initial_function(*args, **kwargs):
            print("opening.....")
            function_name(*args, **kwargs)
            print(f"merong kang {self.__laman}")
            print("closing.....")
        return initial_function
xmas_gift = Regalo("robot", "red")

@xmas_gift.buksan
def tatanggap(name, age):
    print(f"ito ay para kay {name} {age}")
    
@xmas_gift.buksan
def nagpadala(name):
    print(f"Ang nagpadala ay si {name}")
nagpadala("qwerty")
tatanggap("jobert", 20)
