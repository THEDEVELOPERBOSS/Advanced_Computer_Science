# Parent class
class Animal:
    def __init__(self, name, size):
        self.name = name
        self.size = size
# Child classes
class Horse(Animal):
    def __init__(self, name, size, speed): # gets stuff from the parent class 
        super().__init__(name, size)
        self.speed = speed
    def introduce(self):
        print(f"{self.name} is a {self.speed}, {self.size} horse")
class Dog(Animal):
    def __init__(self, name, size, noise):
        super().__init__(name, size)
        self.noise = noise
    def introduce(self):
            print(f"{self.name} is a {self.noise}, {self.noise} dog")
class Mouse(Animal):
    def __init__(self, name, size, sniff):
        super().__init__(name, size)
        self.sniff = sniff
    def introduce(self):
            print(f"{self.name} is a {self.size} mouse that can smell cheese from up to {self.sniff} feet away")
# Objects
obj_1 = Horse("Thunder", "large", "fast")
obj_2 = Dog("Buddy", "large", "quiet")
obj_3 = Mouse("Squeaky", "small", 100)
# Displays information 
Horse.introduce(obj_1)
Dog.introduce(obj_2)
Mouse.introduce(obj_3)