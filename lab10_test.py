from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from product_factory import ProductFactory
from order_line import OrderLine
from digital_product import DigitalProduct
from discount_strategy import BulkDiscount, PercentageDiscount, StudentDiscount
from inventory import Inventory
from FileHandling import load_products

def test_section_2() -> None:
    print("=== Section 2.3: Strategy Pattern Predict First ===")
    supp = Supplier("S001", "Tech Supplier", "sales@tech.com")
    # Note: Using your current Lab 8 PhysicalProduct constructor signature
    item = PhysicalProduct("P001", "Monitor", 250.0, 5, 3.0, supp)

    order = Order("ORD-01", BulkDiscount(200, 20))
    order.add_order_line(item, 1)
    print("With BulkDiscount(200, 20):", order.calculate_total())

    order.set_discount(PercentageDiscount(10))
    print("After set_discount(PercentageDiscount(10)):", order.calculate_total())

    order.set_discount(StudentDiscount(5))
    print("After set_discount(StudentDiscount(5)):", order.calculate_total())



def test_section_3() -> None:
    print("\n=== Section 3.2: Factory Pattern Predict First ===")
    supp = Supplier("S001", "Tech Supplier", "sales@tech.com")

    p1 = ProductFactory.create("physical", "P001", "Laptop", 1200.0, 10, 2.5, supp)
    p2 = ProductFactory.create("digital", "D001", "Photo Editor", 49.9, 100, 500.0, supp)
    print("Created physical:", type(p1).__name__, "| Fulfilment:", p1.get_fulfilment_info())
    print("Created digital:", type(p2).__name__, "| Fulfilment:", p2.get_fulfilment_info())

    try:
        ProductFactory.create("service", "S001", "Installation", 30.0, 5, 0.0, supp)
    except ValueError as e:
        print("Caught expected ValueError:", e)

def test_section_4() -> None:
    print("\n=== Section 4: Validation Tests ===")
    supp = Supplier("S001", "Tech Supplier", "sales@tech.com")

    for label, fn in [
        ("Price <= 0", lambda: ProductFactory.create("physical", "P1", "Desk", 0, 5, supp)),
        ("Negative stock", lambda: ProductFactory.create("digital", "D1", "App", 10.0, -2, supp)),
        ("OrderLine qty <= 0", lambda: OrderLine(ProductFactory.create("digital", "D1", "App", 10.0, 5, supp), 0)),
    ]:
        try:
            fn()
        except ValueError as e:
            print(f"{label} raised ValueError: {e}")


def test_section_5() -> None:
    print("\n=== Section 5.2: CSV Loader Predict First ===")
    supp = Supplier("S001", "Tech Supplier", "sales@tech.com")
    inv = Inventory()

    print("--- Loading existing products.csv ---")
    load_products("products.csv", inv, supp)
    print("IDs in inventory:", [p.get_product_id() for p in inv.get_all_products()])

    print("\n--- Loading missing file ---")
    load_products("missing.csv", inv, supp)

if __name__ == "__main__":
    test_section_2()
    test_section_3()
    test_section_4()
    test_section_5()