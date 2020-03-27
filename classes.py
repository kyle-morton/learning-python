class Product(object):
    price: float
    name: str
    id: int

    def __init__(self):
        self.price = 250
        self.name = 'Xbox One'
        self.id = 1

    def updatePrice(self, newPrice):
        self.price = newPrice

    def __str__(self):
        return self.id.__str__() + ' ' + self.name + ' ' + self.price.__str__()

    
product = Product()
print(product)
product.updatePrice(20)
print(product)
    

class InheritedProduct(Product):
    description: str

    def __init__(self): 
        self.price = 250
        self.name = 'Playstation 4'
        self.id = 2
        self.description = 'PS4 Gaming System'

newProduct = InheritedProduct()
print(newProduct)
newProduct.updatePrice(300)
print(newProduct)