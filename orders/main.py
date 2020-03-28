from models.product import Product
from models.order import Order

prod1 = Product(250.00, 'Xbox One', 1)
prod2 = Product(300.00, 'PS4 Pro', 2)

order = Order()
order.addItem(prod1)
print(order)

order.addItem(prod2)
print(order)