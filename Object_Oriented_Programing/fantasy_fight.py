import random 

class Character: 
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
    def attack(self, opponent):
        random_num = random.randint(1,10)
        opponent.health -= random_num
    def heal(self):
        self.health += 5
    def display(self):
        print(f"{self.name} has {self.health}. They use a {self.weapon.name} and have {self.special_ability}")

class Weapon:
    def __init__(self, name):
        self.name = name

class Orc(Character):
    def __init__(self, name, health, weapon, rage):
        super().__init__(name, health, weapon)
        self.rage = rage
        self.special_ability = "Rage Attack"
    def rage_attack(self, opponent):
        print("RAGE ATTACK STARTED")
        random_num = random.randint(11,20)
        if self.rage >= 3:
            opponent.health -= (random_num + self.rage)
            self.rage = 0 
        else:
            print("Attack failed. Turn lost")
class Elf(Character):
    def __init__(self, name, health, weapon, magic):
        super().__init__(name, health, weapon)
        self.magic = magic
        self.special_ability = "Magic attack"
    def magic_attack(self, opponent):
        print("MAGIC ATTACK ACTIVATED")
        if self.magic >= 3:
            random_num = random.randint(11,20)
            opponent.health -= (random_num + self.magic)
            self.magic = 0
        else:
            print("Attack failed. Turn lost")
orc_weapon = Weapon("Axe")
elf_weapon = Weapon("Bow")
   
def battle():
    orc_name_input = input("What is the orcs name? ")
    orc_health_input = int(input(f"What is {orc_name_input}'s starting health? "))
    elf_name_input = input("What is the elf's name: ")
    elf_health_input = int(input(f"What is {elf_name_input}'s starting health? "))

    orc = Orc(orc_name_input, orc_health_input, orc_weapon, 0)
    elf = Elf(elf_name_input, elf_health_input, elf_weapon, 0)      
    
    while orc.health > 0 and elf.health > 0:
        print("Orcs turn: 1. Attack, 2. Heal, 3. Use Special attack")
        user_input = int(input(""))
        if user_input == 1:
            orc.attack(elf)
        elif user_input == 2:
            orc.heal()
        elif user_input == 3:
            orc.rage_attack(elf)
        if elf.health <= 0:
            break
        orc.display()
        elf.display()
        print("Elfs turn: 1. Attack, 2. Heal, 3. Use Special attack")
        user_input = int(input(""))
        if user_input == 1:
            elf.attack(orc)
            orc.rage += 1 
        elif user_input == 2:
            elf.heal()
            elf.magic += 2
        elif user_input == 3:
            elf.magic_attack(orc)
            orc.rage += 1 
        orc.display()
        elf.display()
        if orc.health <= 0:
            break
    if orc.health <= 0:
        print(f"{elf.name} wins!")
    else:
        print(f"{orc.name} wins!")  
                
battle()