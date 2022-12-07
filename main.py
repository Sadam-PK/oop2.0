from phone import Phone

# item1 = 1
# item2 = 1.2
# item3 = 'apple'
#
# print(type(item1))
# print(type(item2))
# print(type(item3))


# item1 = Item('Apple', 10, 2)
# # item1.apply_discount()
#
# item2 = Item('Banana', 5, 3)
#
# item3 = Item('Grapes', 12, 2)
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
# Item.instantiate_from_csv()
# print(Item.all)


phone1 = Phone('A8000', 8000, 2, 0)
# print(Item.all)
print(Phone.all)
