from .product import Product

class Order(object):
    items: list

    def __init__(self):
        self.items = []
    
    def addItem(self, item: Product):
        self.items.append(item)

    def __str__(self):
        return ",".join(map(str, self.items))