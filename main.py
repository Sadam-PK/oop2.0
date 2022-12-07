# item1 = 1
# item2 = 1.2
# item3 = 'apple'
#
# print(type(item1))
# print(type(item2))
# print(type(item3))

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def price_calc(self, x, y):
        return x * y


item1 = Item('Apple', 10, 2)
print(item1.name, item1.price_calc(item1.price, item1.quantity))
