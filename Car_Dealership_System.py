class Vehicle:
    all_vehicles = [] 
    # attributes
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
    # adds a car 
    def add_car():
        # gets info about the car
        input_make = input("What is the make? ").strip()
        input_model = input("What is the model? ").strip()
        input_year = int(input("What is the year? "))
        input_num_wheels = int(input("How many wheels? "))
        input_seating_capacity = int(input("How many seats? "))
        input_top_speed = int(input("What is its top speed? "))
        # adds it to the vehicle class
        Vehicle(
            input_make,
            input_model,
            input_year,
            input_num_wheels,
            input_seating_capacity,
            input_top_speed
        )

        print(f"{input_make} {input_model} was added.")
        main()
    def remove_car():
        # if there are no veichles available
        if not Vehicle.all_vehicles:
            print("There are no cars to remove.")
            main()
            return
        # removes car user asked for
        print("Which car would you like to remove?")
        for number, car in enumerate(Vehicle.all_vehicles, start=1):
            print(f"{number}. {car.make} {car.model}")
        choice = int(input("Enter the car number: "))
        removed_vehicle = Vehicle.all_vehicles.pop(choice - 1)
        print(f"{removed_vehicle.make} {removed_vehicle.model} was removed.")

        main()
    def display_all():
        # displays all the info about all the car
        for vehicle in Vehicle.all_vehicles:
            print(
                f"{vehicle.make} {vehicle.model}, "
                f"{vehicle.year}, {vehicle.num_wheels} wheels, "
                f"{vehicle.seating_capacity} seats, "
                f"{vehicle.top_speed} mph"
            )
        main()
    
def main():
    # Main UI
    print("\n1. Display info about a car")
    print("2. Add a car to the inventory")
    print("3. Remove a car from the inventory")
    print("4. Display all the cars")
    print("Q. Quit the program")
    
    user_input = input().strip()
    if user_input == '1':
        Vehicle.display_info()
    elif user_input == '2':
        Vehicle.add_car()
    elif user_input == '3':
        Vehicle.remove_car()
    elif user_input == "4":
        Vehicle.display_all()
    elif user_input.lower() == 'q':
        quit()
    

# Cars
ford_raptor = Vehicle("Ford", "Raptor", 2026, 4, 5, 150)
jeep_xj = Vehicle("Jeep", "Cheorkee", "2001", 4, 5, 100)


if __name__ == "__main__":
    main()