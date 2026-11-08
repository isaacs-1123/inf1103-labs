from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier

class Inventory:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Add an existing Product object to the inventory."""
        self.products.append(product)

    def remove_product(self, product_id: str) -> None:
        """Remove the matching Product reference from the inventory."""
        for product in self.products:
            if product.get_product_id() == product_id: 
                self.products.remove(product)
                break

    def find_product(self, product_id: str) -> Product | None:
        """Return the matching Product, or None if it cannot be found."""
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_stock(self, product_id: str, quantity: int) -> None:
        product = self.find_product(product_id)
        if product is not None:
            product.update_stock(quantity)

    def get_all_products(self) -> tuple[Product, ...]:
        return tuple(self.products)

    def to_record(self) -> list[dict]:
        records = []
        for product in self.products:
            base_data = {
                "id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock(),
                "supplier_id": product.get_supplier().get_supplier_id(), 
                "supplier_name": product.get_supplier().get_name(),
                "supplier_email": product.get_supplier().get_contact_email()
            }
            if isinstance(product, PhysicalProduct):
                base_data["type"] = "physical"
                base_data["weight"] = product.get_weight()
            elif isinstance(product, DigitalProduct):
                base_data["type"] = "digital"
                base_data["download_size"] = product.get_download_size()
            
            records.append(base_data)
        return records

    def load_records(self, records: list[dict]) -> None:
        for item in records:
            supp = Supplier(
                item.get("supplier_id", "S000"), 
                item.get("supplier_name", "Unknown"), 
                item.get("supplier_email", "unknown@email.com")
            )
            
            if item.get("type") == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item.get("download_size", 0.0), supp)
            else:
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item.get("weight", 0.0), supp)
            
            self.add_product(product)