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
    def __init__(self, make, model, top_speed, range, time_to_fill, emissions): # gets stuff from the parent class 
        super().__init__(make, model, top_speed, range, time_to_fill)
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill
        self.emissions = emissions
        
    def burnout(self):
        print(f"The {self.make} {self.model} did a burnout. It's emissions are eve worse now and are considered {self.emissions}. But thats ok.")
class EV(Vehicle):
    def __init__(self, make, model, top_speed, range, time_to_fill, wind):
        super().__init__(make, model, top_speed, range, time_to_fill)
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill
        self.wind = wind
        
    def range_hurt(self):
        self.range -= 10
        print(f"The {self.make} {self.model} encoutered {self.wind} of wind! Range dropped 100 miles and is now at {self.range}.\n displaying this message took 5% of your batery")
class Hyrdrogen(Vehicle):
    def __init__(self, make, model, top_speed, range, time_to_fill): 
        super().__init__(make, model, top_speed, range, time_to_fill)
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill

obj_1 = Gas
obj_2 = EV
obj_3 = Hyrdrogen



gas.distance_to_empty()