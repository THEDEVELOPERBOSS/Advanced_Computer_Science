import random 

class Character: 
    def __init__(self, name, health, weapon, special_ablitiy):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.special_ability = special_ablitiy
    def attack(self):
        random_num = random.randint(1,10)
    def heal(self):
        self.heal() += 5
    def display(self):
        print(f"{self.name} has {self.health}. They use a {self.weapon} and have {self.special_ability}")

class Weapon:
    def __init__(self, name):
        self.name = name

class Orc:
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
        self.name = name 
        self.health = health
        self.weapon = weapon 
class Elf:
    def __init__(self, name, health, weapon):
        super().__init__(name, health, weapon)
        self.name = name 
        self.health = health
        self.weapon = weapon
        
def battle():
    orc_name_input = input("What is the orcs name? ")
    orc_health_input = input(f"What is {orc_name_input}'s starting health? ")
    Orc.name = orc_name_input
    Orc.health = orc_health_input
    elf_name_input = input("What is the elf's name: ")
    elf_health_input = input(f"What is {elf_name_input}'s starting health? ")
    Elf.name = elf_name_input
    Elf.health = elf_health_input

