#!/usr/bin/env python3

class CashRegister:
   def __init__(self, discount=0):
        self.total = 0
        self.items = []
        self.previous_transactions = []
        self.discount = discount

   def add_item(self, title, price, quantity=1):
        # Increase total
        self.total += price * quantity

        # Add item multiple times if quantity > 1
        for _ in range(quantity):
            self.items.append(title)

        # Store transaction for voiding
        self.previous_transactions.append(price * quantity)

   def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        # Calculate new total correctly
        self.total = self.total - (self.total * self.discount / 100)

        # Remove decimal if whole number
        if self.total.is_integer():
            self.total = int(self.total)

        print(f"After the discount, the total comes to ${self.total}.")


   def void_last_transaction(self):
        # If no transactions
        if len(self.previous_transactions) == 0:
            return

        # Subtract last transaction from total
        self.total -= self.previous_transactions.pop()
