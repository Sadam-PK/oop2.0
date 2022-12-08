import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name, price, quantity):
        assert price >= 0, f'Price should be more than 0'
        assert quantity >= 0, f'Quantity should be more than 0'
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # #Property decorator = Read only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def price_calc(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

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
        return f"{self.__class__.__name__}('{self.name}', '{self.price}', {self.quantity})"
