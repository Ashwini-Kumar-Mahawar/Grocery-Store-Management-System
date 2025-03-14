from grocery_store import GroceryStore  # Import the GroceryStore class
from item import Item

def main():
    store = GroceryStore()
    sales = []

    while True:
        print("\nGrocery Store Management System")
        print("1. Add Item")
        print("2. Update Item Quantity")
        print("3. Sell Item")
        print("4. Generate Inventory Report")
        print("5. Generate Sales Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_id = input("Enter Item ID: ")
            name = input("Enter Item Name: ")
            price = float(input("Enter Item Price: "))
            quantity = int(input("Enter Item Quantity: "))
            item = Item(item_id, name, price, quantity)
            store.add_item(item)
            print("Item added successfully!")

        elif choice == '2':
            item_id = input("Enter Item ID: ")
            quantity = int(input("Enter Quantity to Add: "))
            if store.update_item_quantity(item_id, quantity):
                print("Item quantity updated successfully!")
            else:
                print("Item not found!")

        elif choice == '3':
            item_id = input("Enter Item ID: ")
            quantity = int(input("Enter Quantity to Sell: "))
            for item in store.inventory:
                if item.item_id == item_id:
                    if store.sell_item(item_id, quantity):
                        sales.append((item_id, quantity, item.price))
                        print("Item sold successfully!")
                    break

        elif choice == '4':
            print("\nInventory Report:")
            store.generate_inventory_report()

        elif choice == '5':
            print("\nSales Report:")
            store.generate_sales_report(sales)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")


# Entry point of the program
if __name__ == "__main__":
    main()