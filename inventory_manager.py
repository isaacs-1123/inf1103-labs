import json
INVENTORY_FILE = "inventory.json"  



def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:  
            print("inventory.json found.") 
            print("Inventory loaded successfully.")  
            return json.load(file)  
    except FileNotFoundError:
        print("inventory.json not found. Starting with empty inventory.")
        return []
    except json.JSONDecodeError:
        print(
            "Error: inventory.json is corrupted or empty. Starting with empty inventory."
        )
        return []


def search_product(inventory, product_id):
    for product in inventory: 
        if product.get("id").upper() == product_id.upper():
            return product
    return None 


def add_product(inventory, product_id, name, price, stock):
    if search_product(inventory, product_id) is not None:  
        return False

    new_product = {
        "id": product_id,  
        "name": name,  
        "price": float(price), 
        "stock": int(stock),  
    }
    inventory.append(new_product)  
    return True  


def display_all(inventory):
    print("\nCurrent Inventory")  
    for item in inventory:  
        print(
            f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
        )  


def main():
    inventory = []  
    exit_program = False

    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    if not inventory:
        add_product(inventory, "P001", "Laptop", 1200.00, 15) 
        add_product(inventory, "P002", "Mouse", 25.50, 40)  
        add_product(inventory, "P003", "Keyboard", 45.00, 25)  

    display_all(inventory)  


if __name__ == "__main__":
    main()  