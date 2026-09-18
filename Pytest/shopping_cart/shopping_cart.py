class ShoppingCart():
    def __init__(self, items):
        self.items = items
        
        
    def add(self, item):
        self.items.append(item)
        
    def remove(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        else:
            return False
    def size(self):
        total_items = len(self.items)
        return total_items
        
    def display_items(self):
        print(self.items)