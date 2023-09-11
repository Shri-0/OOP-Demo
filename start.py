import csv


class Item:

    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Assign Self Object

        # Run validations
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        # return x * y
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point 0
        # 5.0, 10.0
        if isinstance(num, float):
            # count floats that are .0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"


class Phone(Item):
    all = []

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
        Phone.all.append(self)


phone1 = Item("jscPhonev10", 500, 5)
# phone1.broken_phones = 1
print(phone1.calculate_total_price())
phone2 = Item("jscPhonev20", 700, 5)
# phone2.broken_phones = 1


# Item.instantiate_from_csv()
# print("\n")

# print(Item.all)
# print("\n")

# print(Item.is_integer(7.0))


# for instance in Item.all:
#   print(instance.name)

# print (Item.all)
# item1 = Item("Phone", 100, 1)
# item1.apply_discount()
# print(item1.price)

# item2 = Item("Laptop", 1000, 3)
# item2.pay_rate = 0.7
# item2.apply_discount()

# print(item2.price)
# item2 = Item("Laptop", 1000, 3)
