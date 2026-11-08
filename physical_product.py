from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    # Notice the supplier parameter added at the end here!
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight

    def get_weight(self) -> float:
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f" | Weight: {self.__weight}kg")

    def calculate_shipping_cost(self) -> float:
        return 5.0 + (2.0 * self.__weight)

    def get_fulfilment_info(self) -> str:
        return "Requires physical shipping."