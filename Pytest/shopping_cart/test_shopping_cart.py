from shopping_cart import ShoppingCart

def test_add_item_and_size():
    cart = ShoppingCart([]) # Creates the list
    cart.add("Apple") # Adds apple to the list
# remember create object → use object → check result   
    assert cart.size() == 1 # Checks to make sure the cart contains one item
    
def test_remove_item_succes():
    cart = ShoppingCart([]) # Creates the list
    cart.add("Banana") # Adds banana to the list
    assert cart.remove("Banana") == True # Removes banana from the list
    assert "Banana" not in cart.items
    assert cart.size() == 0 # Checks to make sure the cart contains zero items
    
    
    