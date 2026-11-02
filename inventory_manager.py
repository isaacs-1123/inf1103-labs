from product import Product
from inventory import Inventory
from FileHandling import load_inventory, save_inventory

def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = Inventory()
    
    records = load_inventory()
    inventory.load_records(records)

    if not inventory.get_all_products():
        inventory.add_product(Product("P001", "Laptop", 1200.00, 15))
        inventory.add_product(Product("P002", "Mouse", 25.50, 40))
        inventory.add_product(Product("P003", "Keyboard", 45.00, 25))

    exit_program = False
    
    while not exit_program:
        print("\n----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")
        
        choice = input("\nEnter menu option: ")
        
        if choice == "1":
            print("\nCurrent Inventory")
            print("-" * 40)
            for product in inventory.get_all_products():
                print(f"ID: {product.get_product_id()} | Name: {product.get_name()} | Price: ${product.get_price():.2f} | Stock: {product.get_stock()}")
            print("-" * 40)

        elif choice == "2":
            print("\nAdd New Product")
            product_id_input = input("Product ID: ")
            
            if inventory.search_product(product_id_input):
                print("\nError: Product ID already exists. Use Update Stock instead.")
                continue
                
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
                
                new_product = Product(product_id_input, name, price, stock)
                if inventory.add_product(new_product):
                    print("\nProduct added successfully!")
            except ValueError:
                print("\nInvalid input! Price must be a float and stock an int.")

        elif choice == "3":
            print("\nUpdate Stock")
            product_id_input = input("Enter Product ID: ")
            
            product = inventory.search_product(product_id_input)
            if product:
                print("\nProduct Found:")
                print(f"ID: {product.get_product_id()} | Name: {product.get_name()} | Price: ${product.get_price():.2f} | Stock: {product.get_stock()}")
                try:
                    new_stock = int(input("\nNew Stock Quantity: "))
                    inventory.update_stock(product_id_input, new_stock)
                    print("\nStock updated successfully!")
                except ValueError:
                    print("\nInvalid input!")
            else:
                print("\nProduct not found.")

        elif choice == "4":
            print("\nSearch Product")
            product_id_input = input("Enter Product ID: ")
            
            product = inventory.search_product(product_id_input)
            if product:
                print("\nProduct Found")
                print("-" * 40)
                print(f"ID: {product.get_product_id()} | Name: {product.get_name()} | Price: ${product.get_price():.2f} | Stock: {product.get_stock()}")
                print("-" * 40)
            else:
                print("\nProduct not found.")

        elif choice == "5":
            print("\nSaving inventory...")
            save_inventory(inventory.to_record())

        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(inventory.to_record())
            print("\nProgram terminated.")
            exit_program = True

        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()