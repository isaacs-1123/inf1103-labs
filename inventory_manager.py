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


def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as file:  
        json.dump(inventory, file, indent=4)  
        print(f"Inventory saved successfully to {INVENTORY_FILE}.")

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

def update_stock(inventory, product_id, new_stock):
    product = search_product(inventory, product_id) 
    if product:
        product["stock"] = int(new_stock) 
        return True 
    return False

def display_all(inventory):
    print("\nCurrent Inventory")  
    print("-" * 40)  
    for item in inventory:  
        print(
            f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}"
        )  
    print("-" * 40)  


def main():
    inventory = []  
    exit_program = False

    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    if not inventory:
        add_product(inventory, "P001", "Laptop", 1200.00, 15) 
        add_product(inventory, "P002", "Mouse", 25.50, 40)  
        add_product(inventory, "P003", "Keyboard", 45.00, 25)  

    while not exit_program:
        choice = input("\nEnter menu option: ")
        if choice == "1":
            display_all(inventory) 

        elif choice == "2":
            print("\nAdd New Product") 
            product_id_input = input("Product ID: ") 
            if search_product(inventory, product_id_input): 
                print("\nError: Product ID already exists. Use Update Stock instead.")
                continue
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: ")) 
            except ValueError:
                print("\nInvalid input! Price must be a float and stock an int.")
                continue
            if add_product(inventory, product_id_input, name, price, stock): 
                print("\nProduct added successfully!") 

        elif choice == "3":
            print("\nUpdate Stock") 
            product_id_input = input("Enter Product ID: ")
            product = search_product(inventory, product_id_input) 
            if product:
                print("\nProduct Found:") 
                print(f"Name: {product['name']}") 
                print(f"Current Stock: {product['stock']}") 
                try:
                    new_stock = int(input("\nNew Stock Quantity: ")) 
                    update_stock(inventory, product_id_input, new_stock)  
                    print("\nStock updated successfully!") 
                except ValueError:
                    print("\nInvalid input!")
            else:
                print("\nProduct not found.") 

        elif choice == "4":
            print("\nSearch Product") 
            product_id_input = input("Enter Product ID: ")
            product = search_product(inventory, product_id_input)  
            if product:
                print("\nProduct Found")  
                print("-" * 40)  
                print(f"ID: {product['id']}")  
                print(f"Name: {product['name']}")  
                print(f"Price: ${product['price']:.2f}")  
                print(f"Stock: {product['stock']}")  
                print("-" * 40) 
            else:
                print("\nProduct not found.")  

        elif choice == "5":
            print("\nSaving inventory...")  
            save_inventory(inventory)  

        elif choice == "6":
            print("\nSaving inventory before exit...")  
            save_inventory(inventory)  
            print("\nThank you for using Inventory Management System.")  
            print("Program terminated.") 
            exit_program = True 

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()  