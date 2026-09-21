from shopping_cart import ShoppingCart

def test_add_item_and_size():
    cart = ShoppingCart([]) # Creates the list
    cart.add("Apple") # Adds apple to the list
# remember create object → use object → check result   
    assert cart.size() == 1 # Checks to make sure the cart contains one item