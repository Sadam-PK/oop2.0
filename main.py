# item1 = 1
# item2 = 1.2
# item3 = 'apple'
#
# print(type(item1))
# print(type(item2))
# print(type(item3))

class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):
        assert price >= 0, f'Price should be more than 0'
        assert quantity >= 0, f'Quantity should be more than 0'
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    # def price_calc(self, x, y):
    #     return x * y

    # # re-write the above fun as follows - self means object is passed as argument, so;
    def price_calc(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', '{self.price}', {self.quantity})"


item1 = Item('Apple', 10, 2)
# item1.apply_discount()

item2 = Item('Banana', 5, 3)

item3 = Item('Grapes', 12, 2)
# #-------- normal actions of adding values and printing them -------
# item2.pay_rate = 0.7
# item2.apply_discount()
#
# print(item1.name, item1.price, item1.quantity)
# print(item2.name, item2.price, item2.quantity)
#
# print(f'Item 1 price = {item1.price_calc()}')
# print(f'Item 2 price = {item2.price_calc()}')

# #-------- printing will ALL -------
#
# for i in Item.all:
#     print(i.name)

# #-------- special presentation ----------
# print(Item.all)
