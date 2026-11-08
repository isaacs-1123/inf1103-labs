from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order

def run_predict_tests():
    print("--- TEST 1: ASSOCIATION (Supplier & Product) ---")
    # Create the supplier and product
    my_supplier = Supplier("S001", "Tech Source", "sales@techsource.com")
    mouse = PhysicalProduct("P001", "Wireless Mouse", 25.50, 50, 0.2, my_supplier)
    
    # Deleting the supplier variable
    del my_supplier
    
    # Proving the product still has access to it
    print("Supplier Name accessed through Product:", mouse.get_supplier().get_name())
    print("Result: Product still holds the Supplier reference!\n")


    print("--- TEST 2: AGGREGATION (Inventory & Product) ---")
    inventory_a = Inventory()
    inventory_b = Inventory()
    
    software = DigitalProduct("D001", "Antivirus", 60.00, 100, 150.5, mouse.get_supplier())
    
    # Add to A, then remove from A
    inventory_a.add_product(software)
    inventory_a.remove_product("D001")
    
    # Prove the product still exists and works
    print("Product Name after removal from Inv A:", software.get_name())
    
    # Add to B
    inventory_b.add_product(software)
    print(f"Product in Inventory B: {inventory_b.products[0].get_name()}\n")

    print("--- TEST 3: COMPOSITION (Order & OrderLine) ---")
    order_1 = Order("ORD-01")
    order_2 = Order("ORD-02")
    
    # Adding the exact same product to two different orders
    order_1.add_order_line(mouse, 2)
    order_2.add_order_line(mouse, 5)
    
    # Retrieve the internally created OrderLines
    line_from_o1 = order_1._order_lines[0]
    line_from_o2 = order_2._order_lines[0]
    
    print("Are the OrderLines the exact same object in memory?", line_from_o1 is line_from_o2)
    print("Are the Products inside them the exact same object in memory?", 
          line_from_o1.get_product() is line_from_o2.get_product())
    print("Result: 2 OrderLines exist, but only 1 Product exists!\n")

if __name__ == "__main__":
    run_predict_tests()