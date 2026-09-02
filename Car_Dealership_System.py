class Vehicle:
    all_vehicles = []

    def __init__(self, make, model, year, num_wheels, seating_capacity, top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.num_wheels = num_wheels
        self.seating_capacity = seating_capacity
        self.top_speed = top_speed

        Vehicle.all_vehicles.append(self)


def display_info(self):
    print(f"It is a {self.make} {self.model} from the year {self.year}. It has {self.num_wheels} of wheels. It can fit {self.seating_capacity} people. It has a top speed of {self.top_speed} mph.")
def add_car():
    print("Add car function")
def remove_car():
    print("Remove car function")
def display_all():
    for vehicle in Vehicle.all_vehicles:
        display_info(vehicle) 
def main():
    print("Main program")

# Cars
ford_raptor = Vehicle("Ford", "Raptor", 2026, 4, 5, 150)
jeep_xj = Vehicle("Jeep", "Cheorkee", "2001", 4, 5, 100)

display_info(ford_raptor)
display_all()
