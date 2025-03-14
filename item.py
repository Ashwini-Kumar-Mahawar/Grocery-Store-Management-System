class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"