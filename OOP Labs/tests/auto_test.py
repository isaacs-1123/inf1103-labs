import os
import tempfile
import unittest
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from product_factory import ProductFactory
from order import Order
from order_line import OrderLine
from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount
from inventory import Inventory
from FileHandling import load_products


class TestLab9(unittest.TestCase):
    def setUp(self) -> None:
        self.supplier = Supplier("S001", "Tech Supplier", "sales@tech.com")
        self.laptop = ProductFactory.create(
            "physical", "P001", "Laptop", 1000.0, 10, 2.5, self.supplier
        )
        self.ebook = ProductFactory.create(
            "digital", "D001", "Python Guide", 50.0, 100, 15.0, self.supplier
        )

    # --- Section 2: Strategy Pattern Tests ---
    def test_no_discount(self) -> None:
        order = Order("ORD-01", NoDiscount())
        order.add_order_line(self.laptop, 1)
        self.assertAlmostEqual(order.calculate_total(), 1000.0)

    def test_percentage_discount(self) -> None:
        order = Order("ORD-02", PercentageDiscount(10))
        order.add_order_line(self.laptop, 1)
        self.assertAlmostEqual(order.calculate_total(), 900.0)

    def test_bulk_discount_applied_and_not_applied(self) -> None:
        order = Order("ORD-03", BulkDiscount(200, 20))
        order.add_order_line(self.ebook, 2)  # $100 < $200 threshold
        self.assertAlmostEqual(order.calculate_total(), 100.0)

        order.add_order_line(self.ebook, 3)  # $250 >= $200 threshold -> $230
        self.assertAlmostEqual(order.calculate_total(), 230.0)

    def test_runtime_discount_swap(self) -> None:
        order = Order("ORD-04", BulkDiscount(200, 20))
        order.add_order_line(self.ebook, 5)  # $250
        self.assertAlmostEqual(order.calculate_total(), 230.0)

        order.set_discount(StudentDiscount(5))
        self.assertAlmostEqual(order.calculate_total(), 237.5)

    # --- Section 3: Factory Pattern Tests ---
    def test_factory_creates_subclasses(self) -> None:
        self.assertIsInstance(self.laptop, PhysicalProduct)
        self.assertIsInstance(self.ebook, DigitalProduct)

    def test_factory_unknown_type_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create("service", "S001", "Install", 30.0, 5, 0.0, self.supplier)

    # --- Section 4: Validation Tests ---
    def test_invalid_product_price_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P002", "Bad Price", 0.0, 5, 1.0, self.supplier)
        with self.assertRaises(ValueError):
            ProductFactory.create("physical", "P003", "Neg Price", -10.0, 5, 1.0, self.supplier)

    def test_negative_stock_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            ProductFactory.create("digital", "D002", "Bad Stock", 10.0, -1, 5.0, self.supplier)
        with self.assertRaises(ValueError):
            self.laptop.update_stock(-3)

    def test_invalid_order_line_quantity_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            OrderLine(self.laptop, 0)
        with self.assertRaises(ValueError):
            OrderLine(self.laptop, -2)

    # --- Section 5: CSV Exception Handling Tests ---
    def test_load_products_skips_invalid_rows(self) -> None:
        csv_content = (
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P001,Desk Lamp,25.00,10\n"
            "digital,D001,Photo Editor,49.90,100\n"
            "service,S001,Installation,30.00,5\n"
            "physical,P002,Office Chair,abc,3\n"
            "physical,P003,Monitor Stand,39.50,7\n"
        )
        with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
            tmp.write(csv_content)
            tmp_path = tmp.name

        try:
            inv = Inventory()
            load_products(tmp_path, inv, self.supplier)
            loaded_ids = [p.get_product_id() for p in inv.get_all_products()]
            self.assertEqual(loaded_ids, ["P001", "D001", "P003"])
        finally:
            os.remove(tmp_path)

    def test_load_products_missing_file_does_not_crash(self) -> None:
        inv = Inventory()
        load_products("non_existent_file_12345.csv", inv, self.supplier)
        self.assertEqual(len(inv.get_all_products()), 0)


if __name__ == "__main__":
    unittest.main()