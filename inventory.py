# At the top of inventory.py, import ProductFactory:
from product_factory import ProductFactory

# Inside load_records(self, records: list[dict]) -> None:
def load_records(self, records: list[dict]) -> None:
    for item in records:
        supp = Supplier(
            item.get("supplier_id", "S000"),
            item.get("supplier_name", "Unknown"),
            item.get("supplier_email", "unknown@email.com")
        )
        p_type = item.get("type", "physical")
        extra = item.get("download_size", 0.0) if p_type == "digital" else item.get("weight", 0.0)
        product = ProductFactory.create(
            p_type, item["id"], item["name"], item["price"], item["stock"], supp, extra=extra
        )
        self.add_product(product)