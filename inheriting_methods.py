class Vehicle:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        
    def start(self):
        print(f"{self.make} {self.model} is starting.")
    def drive(self):
    
    def stop(self):
class Motorcycle(Vehicle):

class Bus(Vehicle):
    
car = Vehicle("Porsche", "911", 183)
m_cycle = Motorcycle("Kawasaki", "Ninja", 130)
bus = Bus("Blue Bird", "Vision", 65)
