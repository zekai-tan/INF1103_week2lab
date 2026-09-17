overstock_limit = 500 #treshold alert
tax_rate = 0.1 #10% tax rate

def get_valid_input():
    user_input = input("Enter stock quantity per delivery or type 'quit': ").strip()
    if user_input.lower() == 'quit':
        return "quit"
    
    if not user_input.isdigit():
        print("Invalid input, Skipping.\n")
        return None
    
    return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * tax_rate

def generate_report(total_units, failed_attempts):
    print(f"Total inventory: {total_units}")
    print(f"Total rejected entries: {failed_attempts}")

def main():
    total_inventory = 0
    processed_entries = 0
    rejected_entries = 0

    print("Enter stock quantity per delivery or type 'quit'")

    while True:
        quantity = get_valid_input()

        if quantity == "quit":
            break

        if quantity is None:
            rejected_entries += 1
            continue

        total_inventory = process_delivery(total_inventory, quantity)
        delivery_tax = calculate_tax(quantity)
        processed_entries += 1

        print(f"Tax for this delivery: {delivery_tax:.2f}")
        print(f"current total inventory: {total_inventory}")

        if total_inventory > overstock_limit:
            print("Warning: Overstock limit exceeded!\n")
            break

    generate_report(total_inventory, rejected_entries)
    print(f"Total processed entries: {processed_entries}")

main()









    
