from product import Product

class Inventory_class:
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
            records.append({
                "id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock()
            })
        return records

    def load_records(self, records):
        for item in records:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
            self.add_product(product)