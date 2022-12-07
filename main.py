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

    # def price_calc(self, x, y):
    #     return x * y

    # # re-write the above fun as follows - self means object is passed as argument, so;
    def price_calc(self):
        return self.price * self.quantity


item1 = Item('Apple', 10, 2)
item2 = Item('Banana', 5, 3)

print(item1.name, item1.price, item1.quantity)
print(item2.name, item2.price, item2.quantity)

print(f'Item 1 price = {item1.price_calc()}')
print(f'Item 2 price = {item2.price_calc()}')
