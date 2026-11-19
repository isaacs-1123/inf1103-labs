from supplier import Supplier
from physical_product import PhysicalProduct
from order import Order
from discount_strategy import BulkDiscount, PercentageDiscount, StudentDiscount

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

if __name__ == "__main__":
    test_section_2()