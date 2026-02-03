#EMMANUEL BARAKA
#REG NO : BSCIT-05-0113/2024
# Initialize an empty dictionary for the inventory
inventory = {}

def add_item(name, quantity):
    # Check if item exists to update or add new
    if name in inventory:
        inventory[name] += quantity
        print(f"Updated {name} quantity to {inventory[name]}.")
    else:
        inventory[name] = quantity
        print(f"Added {name} with quantity {quantity}.")

def get_item(name):
    # Retrieve information about a specific item
    if name in inventory:
        print(f"Item: {name} | Quantity: {inventory[name]}")
    else:
        print(f"Item '{name}' not found in inventory.")

def show_total_quantity():
    # Calculate and display total quantity of all items
    total = sum(inventory.values())
    print(f"\nTotal items in stock: {total}")

