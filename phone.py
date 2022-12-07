from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, broken_phone):
        super().__init__(name, price, quantity)

        assert broken_phone >= 0, f'Broken phones {broken_phone} cant be negative'
        self.broken_phones = broken_phone
