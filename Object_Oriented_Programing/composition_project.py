class ENGINE: # simple class
    def __init__(self, horsepower, displacement, configuration):
        self.horsepower = horsepower
        self.displacement = displacement
        self.configuration = configuration 
    def specs(self):
        print(f"all {self.horsepower} hp has fired up and is at your disposal. Brought to you by a {self.displacement} {self.configuration}")
class MODEL: # simple class 
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def facts(self):
        print(f"it is a {self.year} {self.model}")
class MAKE: # complex class 
    def __init__(self, make, parent_company, model, engine):
        self.make = make
        self.parent_company = parent_company
        self.model = model
        self.engine = engine
    def overview(self):
        print(f"This is {self.make}'s new car. It is made by {self.parent_company}.")
        self.model.facts()
        self.engine.specs()
        
# Declare simple objects
obj_1 = ENGINE(190, 4.0 ,"I6")
obj_2 = MODEL("Cheorkee", 2001)
# Makes complex object 
obj_3 = MAKE("Jeep", "American Motors Corporation (AMC)", obj_2, obj_1)
# Calls overview method 
obj_3.overview()