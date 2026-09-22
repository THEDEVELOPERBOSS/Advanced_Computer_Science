from car_dealer import Car

def test_rent():
    car_rented = Car("Ford", "Fiesta", 2005)
    
    assert car_rented.rent()