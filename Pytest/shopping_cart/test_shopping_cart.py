from shopping_cart import ShoppingCart

def test_add_item_and_size():
    cart = ShoppingCart([]) # Creates the list
    cart.add("Apple") # Adds apple to the list
# remember create object → use object → check result   
    assert cart.size() == 1 # Checks to make sure the cart contains one item
    
def test_remove_item_succes():
    cart = ShoppingCart([])
    cart.add("Banana") # Adds banana to the list
    assert cart.remove("Banana") # Removes banana from the list
    assert "Banana" not in cart.items
    assert cart.size() == 0 # Checks to make sure the cart contains zero items

def test_remove_item_not_in_cart():
    cart = ShoppingCart([])
    cart.add("Orange") # Adds orange to the list
    assert cart.remove("Pear") == False
    assert "Orange" in cart.items

def test_get_num_items():
    cart = ShoppingCart([])
    cart.add("Milk") # adds milk to the cart 
    cart.add("Eggs") # adds eggs to the cart
    assert cart.size() == 2 # Checks to make sure there are 2 items in the cart