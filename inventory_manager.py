import json
import os


def create_default_inventory():
    return [
        {
            "id": "P001",
            "name": "Laptop",
            "price": 1200.00,
            "stock": 15
        },
        {
            "id": "P002",
            "name": "Mouse",
            "price": 25.50,
            "stock": 40
        },
        {
            "id": "P003",
            "name": "Keyboard",
            "price": 45.00,
            "stock": 25
        }
    ]


def display_all(inventory):
    if not inventory:
        print("\nInventory is empty.")
        return

    print("\nCurrent Inventory")
    print("-" * 64)

    for product in inventory:
        print(
            f"ID: {product['id']} | "
            f"Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | "
            f"Stock: {product['stock']}"
        )

    print("-" * 64)

def search_product(inventory):
    product_id = input("Enter Product ID: ").strip().upper()

    for product in inventory:
        if product["id"].upper() == product_id:
            print("\nProduct Found")
            print("-" * 48)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 48)
            return

    print("Product not found.")


def add_product(inventory):
    print("\nAdd New Product")

    product_id = input("Product ID: ").strip().upper()

    for product in inventory:
        if product["id"].upper() == product_id:
            print("A product with this ID already exists.")
            return

    product_name = input("Product Name: ").strip()

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
    except ValueError:
        print("Invalid price or stock quantity. Product was not added.")
        return

    if price < 0 or stock < 0:
        print("Price and stock quantity cannot be negative.")
        return

    new_product = {
        "id": product_id,
        "name": product_name,
        "price": price,
        "stock": stock
    }

    inventory.append(new_product)
    print("Product added successfully!")


def update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter Product ID: ").strip().upper()
    product = next((p for p in inventory if p["id"].upper() == product_id), None)
    if not product:
        print("Product not found.")
        return
    print(f"Product Found:\nName: {product['name']}\nCurrent Stock: {product['stock']}")
    try:
        new_stock = int(input("New Stock Quantity: ").strip())
    except ValueError:
        print("Invalid stock quantity.")
        return
    if new_stock < 0:
        print("Stock quantity cannot be negative.")
        return
    product["stock"] = new_stock
    print("Stock updated successfully!")


def load_inventory():
    try:
        with open("inventory.json", "r") as f:
            inventory = json.load(f)

        print("inventory.json found.")
        print("Inventory loaded successfully.")
        return inventory

    except FileNotFoundError:
        print("inventory.json not found. Starting with default inventory.")
        return create_default_inventory()

    except (json.JSONDecodeError, OSError):
        print("Could not load inventory.json. Starting with default inventory.")
        return create_default_inventory()

def save_inventory(inventory):
    try:
        with open("inventory.json", "w") as f:
            json.dump(inventory, f, indent=4)
        print("Inventory saved successfully to inventory.json.")
    except OSError:
        print("Error: Inventory could not be saved.")


def show_menu():
    print("""
-------- MENU --------
1. Display All Products
2. Add Product
3. Update Stock
4. Search Product
5. Save Inventory
6. Exit
-----------------------""")


def main():
    print("=" * 40, "INVENTORY MANAGEMENT SYSTEM", "=" * 40, sep="\n")
    inventory = load_inventory()
    actions = {"1": display_all, "2": add_product, "3": update_stock, "4": search_product}

    while True:
        show_menu()
        option = input("Enter option: ").strip()
        if option in actions:
            actions[option](inventory)
        elif option in ("5", "6"):
            print("Saving inventory..." if option == "5" else "Saving inventory before exit...")
            save_inventory(inventory)
            if option == "6":
                print("Thank you for using Inventory Management System.\nProgram terminated.")
                break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()