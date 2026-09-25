class Car_dealer():
    def __init__(self, make, model, year, car_rented):
        self.make = make
        self.model = model
        self.year = year
        self.rented = car_rented

    def rent(self):
        if self in cars_in_inventory:
            self.rented = True
            return "Car has been taken out succesfully"
        else:
            return "Car is not in inventory"

    def return_car(self):
        if self.rented and self not in cars_in_inventory:
            self.rented = False
            cars_in_inventory.append(self)
            return "Car has been returned succesfully"
        else:
            return "Car is still in inventory"

    def return_wrong_car(self):
        if self.rented and self not in master_inventory:
            return "This is not one of our cars. You are returning it to the wrong place"
        else:
            return "This is one of our cars"
        
Ford_fiesta = Car_dealer("Ford", "Fiesta", 2005, False)
jeep_xj = Car_dealer("Jeep", "Cheorkee", 2001, True)
cars_in_inventory = [Ford_fiesta]
master_inventory = [Ford_fiesta, jeep_xj]