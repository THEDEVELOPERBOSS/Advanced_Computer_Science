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

# Prints all the info about the selected car
def display_info(vehicle=None):
    print("Available cars:")
    for number, car in enumerate(Vehicle.all_vehicles, start=1):
        print(f"{number}. {car.make} {car.model}")

    choice = int(input("Which car would you like to look at? "))
    vehicle = Vehicle.all_vehicles[choice - 1] # uses - 1 because the list starts to index at 0 but the user will input one ahead of that 

    print(f"It is a {vehicle.make} {vehicle.model} from the year {vehicle.year}. It has {vehicle.num_wheels} wheels. It can fit {vehicle.seating_capacity} people. It has a top speed of {vehicle.top_speed} mph.")
    main()
def add_car():
    print("Add car function")


def remove_car():
    print("Remove car function")
    
def display_all():
    for vehicle in Vehicle.all_vehicles:
        display_info(vehicle)

def main():
    print("\n1. Display info about a car")
    print("2. Add a car to the inventory")
    print("3. Remove a car from the inventory")
    print("4. Display all the cars")
    print("Q. Quit the program")
    
    user_input = input().strip()
    if user_input == '1':
        display_info()
    elif user_input == '2':
        add_car()
    elif user_input == '3':
        remove_car()
    elif user_input == "4":
        display_all()
    elif user_input.lower() == 'q':
        quit()
    

# Cars
ford_raptor = Vehicle("Ford", "Raptor", 2026, 4, 5, 150)
jeep_xj = Vehicle("Jeep", "Cheorkee", "2001", 4, 5, 100)


if __name__ == "__main__":
    main()
