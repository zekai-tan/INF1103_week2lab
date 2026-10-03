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
