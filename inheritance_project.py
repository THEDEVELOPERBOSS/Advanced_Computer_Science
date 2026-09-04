class Vehicle:
    # attributes
    def __init__(self, make, model, top_speed, range, time_to_fill):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill
    def distance_to_empty(self):
        print(f"The {self.make} {self.model} has {self.distance_to_empty} miles left.")
    def time_wasted(self):
        print(f"Your {self.make} {self.model} is going to take {self.time_to_fill} minutes to fill up. If you are mad about this number you shouldn't have gotten an EV.")
        
class Gas(Vehicle):
    
class EV(Vehicle):
    
class Hyrdrogen(Vehicle):

obj_1 = Gas
obj_2 = EV
obj_3 = Hyrdrogen



gas.distance_to_empty()