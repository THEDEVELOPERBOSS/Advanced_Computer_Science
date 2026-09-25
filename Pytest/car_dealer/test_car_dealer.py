from car_dealer import Car_dealer, cars_in_inventory, master_inventory

def test_rent(): 
    car_rented = Car_dealer("Ford", "Fiesta", 2005, False) # desired car
    cars_in_inventory.append(car_rented) # takes it out 

    assert car_rented.rent() == "Car has been taken out succesfully" # makes sure it worked
    
def test_rent_car_out(): # tests to see if you can rent an already rented car
    car_rented = Car_dealer("Jeep", "Cheorkee", 2001, True) 
    
    assert car_rented.rent() == "Car is not in inventory"

def test_return_car(): # returning car
    car_rented = Car_dealer("Jeep", "Cheorkee", 2001, True)

    assert car_rented.return_car() == "Car has been returned succesfully"
    assert car_rented.rented == False # changes status to not being rented
    assert car_rented in cars_in_inventory # makes sure it is in invnentory again

def test_return_car_in(): # tests returning a car that is already returned
    car_rented = Car_dealer("Ford", "Fiesta", 2005, False) 
    cars_in_inventory.append(car_rented)

    assert car_rented.return_car() == "Car is still in inventory"

def test_return_wrong_car(): # returning a car that does not belong to them
    car_rented = Car_dealer("Subaru", "Outback", 2010, True) # creates other car
    assert car_rented.return_wrong_car() == "This is not one of our cars. You are returning it to the wrong place"

def test_add_car(): # adding a car
    new_car = Car_dealer("Ford", "Mustang", 2020, False) # defines new car

    new_car.add_car() # adds it with funciton

    assert new_car in cars_in_inventory # checks to make sure it is in both inventorys
    assert new_car in master_inventory