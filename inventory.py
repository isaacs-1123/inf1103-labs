from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class Inventory:
    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if product.get_product_id() not in self._products:
            self._products[product.get_product_id()] = product
            return True
        return False

    def search_product(self, product_id):
        return self._products.get(product_id)

    def update_stock(self, product_id, quantity):
        product = self.search_product(product_id)
        if product:
            product.update_stock(quantity)

    def get_all_products(self):
        return tuple(self._products.values())

    def to_record(self):
        records = []
        for product in self._products.values():
            base_data = {
                "id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock()
            }
            if isinstance(product, PhysicalProduct):
                base_data["type"] = "physical"
                base_data["weight"] = product.get_weight()
            elif isinstance(product, DigitalProduct):
                base_data["type"] = "digital"
                base_data["download_size"] = product.get_download_size()
            
            records.append(base_data)
        return records

    def load_records(self, records):
        for item in records:
            if item.get("type") == "digital":
                product = DigitalProduct(item["id"], item["name"], item["price"], item["stock"], item.get("download_size", 0.0))
            else:
                product = PhysicalProduct(item["id"], item["name"], item["price"], item["stock"], item.get("weight", 0.0))
            self.add_product(product)