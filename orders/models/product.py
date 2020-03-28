class Product(object):
    price: float
    name: str
    id: int

    def __init__(self, price: float, name: str, id: int):
        self.price = price
        self.name = name
        self.id = id

    def updatePrice(self, newPrice):
        self.price = newPrice

    def __str__(self):
        return self.id.__str__() + ' ' + self.name + ' ' + self.price.__str__()