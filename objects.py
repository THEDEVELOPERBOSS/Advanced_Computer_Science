# Creates a class
class Character:
    # Attributes:
    def __init__(self, name, character_type, health, level, weapon):
        self.name = name
        self.character_type = character_type
        self.health = health
        self.level = level
        self.weapon = weapon
    
    # Methods
    # Method for introducing the character
    def introduce(self):
        print(f"{self.name} is a {self.character_type}")
    # Shows their stats
    def display_stats(self):
        print(f"{self.name} has {self.health} hp left and is at level {self.level}")
    # Attacks another character
    def attack(self):
        print(f"{self.name} attacked with {self.weapon}")
    # Increases level by 1 
    def level_up(self):
        self.level += 1 
        print(f"{self.name} leveled up! They are now at level {self.level}")
    # Reduces health
    def take_damage(self):
        self.health -= 10
        print(f"{self.name} took a hit! Their health is now at {self.health}")
# Defines objects using character class
warrior = Character("Frank", "Warrior", 100, 1, "Sword")
giant = Character("Jonathan", "Giant", 90, 10, "Club")
dragon = Character("Bill", "Dragon", 100, 55, "Fire Breath")
wizard = Character("Merlin", "Wizard", 300, 1000, "Attack Spell")

from objects import Character
    
# Test 1
test_character = Character("Frank", "Warrior", 100, 1, "Sword")
print(f"Name: {test_character.name}")
print(f"Type: {test_character.character_type}")
print(f"Health: {test_character.health}")
print(f"Level: {test_character.level}")
print(f"Weapon: {test_character.weapon}")

# Test 2
hero = Character("Frank", "Warrior", 100, 1, "Sword")
hero.take_damage()
assert hero.health == 90

# Test 3
hero.level_up()
assert hero.level == 2
    
# Test 4
hero.attack()