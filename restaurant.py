class Restaurant:
    def __init__(self, Name, Menu):
        self.name = Name
        self.menu = Menu
    def display_restaurant(self):
        print(f"The name of this restraunt is {self.name} and they serve {self.menu_options}")
    menu_options = []
class Menu:
    def __init__(self, food_options):
        self.food_options = food_options
    def add_item():
        
    def display_menu():
        
class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def display_item(self):
        print(f"{self.name} is a {self.category}. It costs $ {self.price}")
        
