class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year
    
    def rent(self):
        if car_rent in self.cars_in_inventory:
            return("Car has been taken out succesfully")
        else:
            return("Car is not in inventory")