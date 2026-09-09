class ENGINE: # simple class
    def __init__(self, horsepower, displacement, configuration):
        self.horsepower = horsepower
        self.displacement = displacement
        self.configuration = configuration 
    def turn_over(self)
        print(f" all {self.horsepower} hp is at your disposal. Brought to you by a {self.displacement} {self.configuration}")
class MODEL: # simple class 
    def __init__(self, model, year):
        self.model = model
        self.year = year
class MAKE: # complex class 
    def __init__(self, make, parent_company):
        self.make = make
        self.parent_company = parent_company
    
obj_1 = ENGINE(190, 4.0 ,"I6")