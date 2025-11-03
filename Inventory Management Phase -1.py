
# Name = Yash Sharma
# Enrollment No. 2502140095

# Inventory Assignment:

# 1. --- Initial Setup ---

inventory = {
    "P001": {"name": "Pen", "stock_count": 50, "price": 10.50, "category": "Writing"},
    "N002": {"name": "Notebook", "stock_count": 25, "price": 25.00, "category": "Paper"},
    "E003": {"name": "Eraser", "stock_count": 100, "price": 5.00, "category": "General"}
}

# Password for authentication
PASSWORD = "Yash123@"


def authenticate_user():
    attempts = 3
    while attempts >0:
        if input("Enter Password: ") == PASSWORD:
            print("🎊🎉 Access Granted ")
            return True
        attempts -= 1
        print(f"❌ Access Denied ❌. {attempts} Attempts Left")
    print("❌❌ Access Denied ❌❌")
    return False

def display_menu():
    pass

# 2. --- Utility Functions ---

def get_item_details(item_id):
    pass


def print_item(item_id, details):
    pass


# --- 3. CRUD Operations ---

def add_item(inventory):
    pass

def modify_item(inventory):
    pass

def delete_item(inventory):
    pass

def search_item(inventory):
    pass

def view_reports(inventory):
    pass


# After this Main Execution.



