# Parent Class
class Vehicle:
    # Attributes
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
    # Methods     
    def start(self):
        print(f"{self.make} {self.model} is starting.")
    def drive(self):
        print(f"{self.make} {self.model} is driving and accelerating to it's top speed of {self.top_speed}.")
    def stop(self):
        print(f"{self.make} {self.model} is coming to a stop.")
# Child classes
class Motorcycle(Vehicle):
    pass
class Bus(Vehicle):
    pass
# Objects       
car = Vehicle("Porsche", "911", 183)
m_cycle = Motorcycle("Kawasaki", "Ninja", 130)
bus = Bus("Blue Bird", "Vision", 65)
# Displays methods using parent or child class
Vehicle.start(car)
Vehicle.drive(m_cycle)
Vehicle.stop(bus)