from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from FileHandling import load_inventory, save_inventory
from can_be_shipped import CanBeShipped
from supplier import Supplier

def main() -> None:
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = Inventory()
    
    records = load_inventory()
    inventory.load_records(records)

    if not inventory.get_all_products():
        default_supp = Supplier("S001", "Default Electronics", "electronicsales@default.com")
        inventory.add_product(PhysicalProduct("P001", "Laptop", 1200.00, 15, 2.5, default_supp))
        inventory.add_product(PhysicalProduct("P002", "Mouse", 25.50, 40, 0.2, default_supp))
        inventory.add_product(PhysicalProduct("P003", "Keyboard", 45.00, 25, 0.8, default_supp))

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
            print("-" * 80)

            products = inventory.get_all_products()

            for i, product in enumerate(products):
                product.display_information()
                print(f"\n   -> Info: {product.get_fulfilment_info()}")
                print(f"   -> Supplier: {product.get_supplier().get_name()} ({product.get_supplier().get_contact_email()})")
                
                if isinstance(product, CanBeShipped):
                    print(f"   -> Shipping Cost: ${product.calculate_shipping_cost():.2f}")

                if i < len(products) - 1:
                    print("")

            print("-" * 80)

        elif choice == "2":
            print("\nAdd New Product")
            print("1. Physical Product")
            print("2. Digital Product")
            product_type = input("Select product type (1 or 2): ")
            
            if product_type not in ["1", "2"]:
                print("Invalid type selected.")
                continue

            product_id_input = input("Product ID: ")
            
            if inventory.find_product(product_id_input):
                print("\nError: Product ID already exists. Use Update Stock instead.")
                continue
                
            name = input("Product Name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock Quantity: "))
                
                if product_type == "1":
                    weight = float(input("Weight (kg): "))
                else:
                    size = float(input("Download Size (MB): "))

                print("\n-- Supplier Details --")
                s_id = input("Supplier ID: ")
                s_name = input("Supplier Name: ")
                s_email = input("Supplier Email: ")
                new_supplier = Supplier(s_id, s_name, s_email)

                if product_type == "1":             
                    new_product = PhysicalProduct(product_id_input, name, price, stock, weight, new_supplier)
                else:
                    new_product = DigitalProduct(product_id_input, name, price, stock, size, new_supplier)
                
                
                inventory.add_product(new_product)
                print("\nProduct added successfully!")
            except ValueError:
                print("\nInvalid input! Ensure numeric fields are typed correctly.")

        elif choice == "3":
            print("\nUpdate Stock")
            product_id_input = input("Enter Product ID: ")
            
            product = inventory.find_product(product_id_input)
            if product:
                print("\nProduct Found:")
                product.display_information()
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
            
            product = inventory.find_product(product_id_input)
            if product:
                print("\nProduct Found")
                print("-" * 40)
                product.display_information()
                
                print("\nSupplier Details:")
                product.get_supplier().display_information()
                
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