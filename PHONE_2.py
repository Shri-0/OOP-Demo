import csv
from item import Item


class Phone(Item):
    # all = []
    pay_rate = 0.1

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Call to super function to have access to all attributes/methods
        super().__init__(
            name, price, quantity
        )
        # Assign Self Object

        # Run validations
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater than or equal to 0"

        # self.name = name
        # self.price = price
        # self.quantity = quantity
        self.broken_phones = broken_phones

        # actions to execute
        # Phone.all.append(self)


phone1 = Item("jscPhonev10", 500, 5)
# phone1.broken_phones = 1
# print(phone1.calculate_total_price())
# phone2 = Item("jscPhonev20", 700, 5)
# phone2.broken_phones = 1

print(Item.all)
print(Phone.all)
