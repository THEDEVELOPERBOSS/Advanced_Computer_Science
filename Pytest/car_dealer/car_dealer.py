class Car_dealer(): # defines car class
    def __init__(self, make, model, year, car_rented): 
        self.make = make
        self.model = model
        self.year = year
        self.rented = car_rented

    def rent(self): # rent function
        if self in cars_in_inventory: # checks to see if the desired car is in inventory
            self.rented = True # changes the status to be rented
            return "Car has been taken out succesfully"
        else: # what happens if the car is not in the inventory
            return "Car is not in inventory"

    def return_car(self):
        if self.rented and self not in cars_in_inventory: # checks to make the car being returned is not in inventory
            self.rented = False
            cars_in_inventory.append(self) # puts it back into the inventory
            return "Car has been returned succesfully"
        else: # what happens if car is in inventory
            return "Car is still in inventory"

    def return_wrong_car(self): # if someone returns a car that isn't one of the companies
        if self.rented and self not in master_inventory: # checks to see if it is in master list
            return "This is not one of our cars. You are returning it to the wrong place"
        else:
            return "This is one of our cars"
    
def add_car(self): # adding car to inventory
    cars_in_inventory.append(self) # adds to list of cars not rented
    master_inventory.append(self) # adds to master list of all cars
    return master_inventory and cars_in_inventory

new_car = Car_dealer("BLANK", "BLANK", 0000, True) # blank car
Ford_fiesta = Car_dealer("Ford", "Fiesta", 2005, False)
jeep_xj = Car_dealer("Jeep", "Cheorkee", 2001, True)
cars_in_inventory = [Ford_fiesta] # cars not rented
master_inventory = [Ford_fiesta, jeep_xj] # master list of all cars company owns