class CashRegister:
    def __init__(self, discount=None):
        # Allow user input; default to 0 if none given
        self.discount = discount if discount is not None else 0
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        # Must be an int between 0-100 inclusive
        if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            # keep previous value if it exists, otherwise fall back to 0
            self._discount = getattr(self, "_discount", 0)

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return
        self.total -= self.total * (self.discount / 100)
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        for _ in range(last["quantity"]):
            if last["item"] in self.items:
                self.items.remove(last["item"])


if __name__ == "__main__":
    register = CashRegister(discount=20)
    register.add_item("Coffee", 4.50, 1)
    register.add_item("Bagel", 3.00, 2)
    print(register.total, register.items, register.previous_transactions)

    register.apply_discount()
    print("After discount:", register.total, register.previous_transactions)

    register.void_last_transaction()
    print("After void:", register.total, register.items, register.previous_transactions)