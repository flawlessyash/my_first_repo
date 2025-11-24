# Name = Yash Sharma
# Enrollment = 2502140095


# --- 1. SETUP AND DATA ---
# The main inventory dictionary: {item_id: {details}}
inventory = {
    "P001": {"name": "Pen", "stock_count": 50, "price": 10.50, "category": "Writing"},
    "N002": {"name": "Notebook", "stock_count": 25, "price": 25.00, "category": "Paper"},
    "E003": {"name": "Eraser", "stock_count": 100, "price": 5.00, "category": "General"}
}

PASSWORD = "admin"


def authenticate_user():
    """Handles password check with 3 attempts."""
    attempts = 3
    while attempts > 0:
        if input("Enter password: ") == PASSWORD:
            print("\nAccess granted. Welcome!")
            return True
        attempts -= 1
        print(f"Incorrect password. {attempts} attempts remaining.")
    print("Access denied.")
    return False


def display_menu():
    """Prints the main menu options."""
    print("\n--- INVENTORY MANAGEMENT MENU ---")
    print("1. Add New Item")
    print("2. Modify Item Details")
    print("3. Delete Item")
    print("4. View Reports")
    print("5. Search for Item")
    print("6. Exit")
    print("---------------------------------")


def print_item_details(item_id, details):
    """Formats and prints the details of a single item."""
    print(
        f"  ID: {item_id:<5} | Name: {details['name']:<10} | Stock: {details['stock_count']:<5} | Price: ${details['price']:.2f}")


# --- 2. CRUD OPERATIONS (Core Logic) ---
def add_item(inventory):
    """Adds a new item to the inventory dictionary."""
    item_id = input(str.title("Enter new Item ID: "))

    if item_id in inventory:
        print(f"Error: Item with ID '{item_id}' already exists.")
        return

    try:
        name = input("Enter item Name: ")
        stock = int(input("Enter Stock Count: "))
        price = float(input("Enter Price: "))
        category = input("Enter Category: ")


        inventory[item_id] = {"name": name, "stock_count": stock, "price": price, "category": category}
        print(f"Successfully added {name} (ID: {item_id}).")
    except ValueError:
        print("Invalid number format for stock or price. Item not added.")




def modify_item(inventory):
    """Updates stock count or price of an existing item."""
    item_id = input("Enter the ID of the item to modify: ")

    if item_id not in inventory:  # Conditional check
        print(f"Error: Item with ID '{item_id}' not found.")
        return

    print(f"\n--- Modifying {inventory[item_id]['name']} ---")
    print_item_details(item_id, inventory[item_id])


    new_stock = input("Enter NEW stock count (or press Enter to skip): ")
    if new_stock:
        try:
            inventory[item_id]['stock_count'] = int(new_stock)  # Update dictionary value
            print(f"Stock for {item_id} updated.")
        except ValueError:
            print(" Invalid stock count. Stoc  count not modified.")





def delete_item(inventory):
    item_id = input("Enter the ID of the item to delete: ")

    if item_id not in inventory:
        print(f" Error: Item with ID '{item_id}' not found.")
        return

    confirm = input(f"Are you sure you want to delete {inventory[item_id]['name']} (y/n)? ").lower()
    if confirm == 'y':
        del inventory[item_id]
        print(f" Successfully deleted item ID: {item_id}.")
    else:
        print("Deletion cancelled.")


def view_reports(inventory):
    total_value = 0.0
    low_stock_threshold = 5
    low_stock_items = []

    print("\n--- INVENTORY REPORTS ---")

    for item_id, details in inventory.items():
        # Total Stock Value calculation
        total_value += details['stock_count'] * details['price']

        # Low Stock check
        if details['stock_count'] < low_stock_threshold:
            low_stock_items.append(details['name'])

    print(f" Total Inventory Value: ₹{total_value:.2f}")


    print("\n Low Stock Items (Below 5):")
    if low_stock_items:
        print("  " + ", ".join(low_stock_items))
    else:
        print("  None. Stock levels are healthy!")


def search_item(inventory):
    query = input("Enter item name or ID to search for: ").lower()
    found_count = 0

    print(f"\n--- Search Results for '{query}' ---")

    for item_id, details in inventory.items():

        if query in item_id.lower() or query in details['name'].lower():
            print_item_details(item_id, details)
            found_count += 1

    if found_count == 0:
        print(f"No items found matching '{query}'.")


# --- 3. MAIN EXECUTION ---
if authenticate_user():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            modify_item(inventory)
        elif choice == '3':
            delete_item(inventory)
        elif choice == '4':
            view_reports(inventory)
        elif choice == '5':
            search_item(inventory)
        elif choice == '6':
            print("Exiting program. Data is lost (Phase 1 limitation). Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")




