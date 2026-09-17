class ShoppingCart():
    def __init__(self, items):
        self.items = items
        
        cart = ShoppingCart(["apple", "bread", "milk"])
        print(cart.items)
        
    def add(cart):
        cart.append("eggs")
        
    def remove(cart):
        cart.remove("apple")
    
    def size(cart):
        total_items = len(cart)
        print(f"{total_items} in the cart")
        
    def display_items():
        