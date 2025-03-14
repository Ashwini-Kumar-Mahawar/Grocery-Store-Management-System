from item import Item  # Import the Item class

class GroceryStore:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def update_item_quantity(self, item_id, quantity):
        for item in self.inventory:
            if item.item_id == item_id:
                item.quantity += quantity
                return True
        return False

    def sell_item(self, item_id, quantity):
        for item in self.inventory:
            if item.item_id == item_id:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    return True
                else:
                    print("Not enough stock!")
                    return False
        print("Item not found!")
        return False

    def generate_inventory_report(self):
        for item in self.inventory:
            print(item)

    def generate_sales_report(self, sales):
        total_sales = 0
        for item_id, quantity, price in sales:
            total_sales += quantity * price
        print(f"Total Sales: ${total_sales}")