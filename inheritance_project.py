# Parent car class
class Vehicle:
    # attributes
    def __init__(self, make, model, top_speed, range, time_to_fill):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill
    # Methods
    def distance_to_empty(self):
        print(f"The {self.make} {self.model} has {self.distance_to_empty} miles left.")
    def time_wasted(self):
        print(f"Your {self.make} {self.model} is going to take {self.time_to_fill} minutes to fill up. If you are mad about this number you shouldn't have gotten an EV.")
        
# Gas car child class 
class Gas(Vehicle):
    def __init__(self, make, model, top_speed, range, time_to_fill, emissions): # adds on attribute
        super().__init__(make, model, top_speed, range, time_to_fill) # Inheriting attributes
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill
        self.emissions = emissions # Defines new attribute
        
    def burnout(self):
        print(f"The {self.make} {self.model} did a burnout. It's emissions are eve worse now and are considered {self.emissions}. But thats ok.")
# EV car child class 
class EV(Vehicle):
    def __init__(self, make, model, top_speed, range, time_to_fill, wind):
        super().__init__(make, model, top_speed, range, time_to_fill)
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill
        self.wind = wind
        
    def hurt_range(self):
        self.range -= 10
        print(f"The {self.make} {self.model} encoutered {self.wind} of wind! Range dropped 100 miles and is now at {self.range}.\n displaying this message took 5% of your batery")
# Hydrogen car child class
class Hyrdrogen(Vehicle):
    def __init__(self, make, model, top_speed, range, time_to_fill, temp): 
        super().__init__(make, model, top_speed, range, time_to_fill)
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.range = range
        self.time_to_fill = time_to_fill
        self.temp = temp
        
    def heat(self):
        print(f"{self.make} {self.model} lost its hyrdrogen to it being {self.temp} degrees fahrenheit outside.")
# Declares the objects
obj_1 = Gas("Jeep", "Cheorkee", "100", 250, "2 minutes", "meh")
obj_2 = EV("Tesla", "Model S", "190", 300, "3 hours", "2 mph")
obj_3 = Hyrdrogen("Toyota", "Mirai", 150, "150", "10 minutes", "80")


Gas.burnout(obj_1)
EV.hurt_range(obj_2)
Hyrdrogen.heat(obj_3)

