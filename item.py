import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):
        assert price >= 0, f'Price should be more than 0'
        assert quantity >= 0, f'Quantity should be more than 0'
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # #Property decorator = Read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        self.__quantity = value

    def price_calc(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for i in items:
            Item(
                name=i.get('name'),
                price=float(i.get('price')),
                quantity=int(i.get('quantity')),
            )

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.__price}', {self.__quantity})"
