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


total_inventory = 0
processed_entries = 0
rejected_entries = 0

print("Enter stock quantity per delivery or type 'quit'")

while True:
    user_input = input("Stock quantity: ").strip() #remove whitespace
    if user_input.lower() == 'quit':
        print("\nInvalid") #\n makes a newline
        break

    if not user_input.isdigit(): #returns true only for positive whole numbers
        print("Invalid input, Skipping.\n")
        rejected_entries += 1
        continue

    quantity = int(user_input)
    if quantity < 0:
        print("Invalid input, Skipping.\n")
        rejected_entries += 1
        continue

    total_inventory += quantity
    processed_entries += 1
    print(f"Current total inventory: {total_inventory}") #f replaces variables in the string

    if total_inventory > overstock_limit:
        print("Warning: Overstock limit exceeded!\n")
        break

print(f"total inventory: {total_inventory}")
print(f"Total processed entries: {processed_entries}")
print(f"Total rejected entries: {rejected_entries}")









    
