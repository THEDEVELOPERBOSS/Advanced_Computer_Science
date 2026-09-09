class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_item(self):
        print(f"{self.name} is a {self.category}. It costs ${self.price:.2f}")


class Menu:
    def __init__(self):
        self.food_options = []

    def add_item(self, item):
        self.food_options.append(item)

    def display_menu(self):
        print("Menu:")
        for item in self.food_options:
            item.display_item()


class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu

    def display_restaurant(self):
        print(f"The name of this restaurant is {self.name}.")
        self.menu.display_menu()


obj1 = MenuItem("Meatballs", 10.99, "Mains")
obj2 = MenuItem("Steak", 25.00, "Mains")
obj3 = MenuItem("Fries", 7.00, "Sides")
obj4 = MenuItem("Chicken Salad", 15.00, "Salad")
obj5 = MenuItem("Burger", 16.99, "Mains")
obj6 = MenuItem("Cheesecake", 24.99, "Desserts")
obj7 = MenuItem("Cookies", 50.00, "Desserts")
obj8 = MenuItem("Chips", 13.99, "Sides")

menu = Menu()
fancy_place = Restaurant("Money Disappear", menu)

menu.add_item(obj1)
menu.add_item(obj2)
menu.add_item(obj3)
menu.add_item(obj4)
menu.add_item(obj5)
menu.add_item(obj6)
menu.add_item(obj7)
menu.add_item(obj8)

fancy_place.display_restaurant()