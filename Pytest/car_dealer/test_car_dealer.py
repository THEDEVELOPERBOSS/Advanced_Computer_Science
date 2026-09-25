from car_dealer import Car_dealer, cars_in_inventory

def test_rent():
    car_rented = Car_dealer("Ford", "Fiesta", 2005, False)
    cars_in_inventory.append(car_rented)

    assert car_rented.rent() == "Car has been taken out succesfully"
    
def test_rent_car_out():
    car_rented = Car_dealer("Jeep", "Cheorkee", 2001, True)
    
    assert car_rented.rent() == "Car is not in inventory"

def test_return_car():
    car_rented = Car_dealer("Jeep", "Cheorkee", 2001, True)
    
    assert car_rented.return_car() == "Car has been returned succesfully"

def test_return_car_in():
    car_rented = Car_dealer("Ford", "Fiesta", 2005, False)
    cars_in_inventory.append(car_rented)

def test_return_wrong_car():
    car_rented = Car_dealer("Subaru", "Outback", 2010, True)
    assert car_rented.return_wrong_car() == "This is not one of our cars. You are returning it to the wrong place"