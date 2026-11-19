from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        extra_value: float = 0.0,
        supplier: Supplier | None = None
    ) -> Product:
        if supplier is None:
            supplier = Supplier("S000", "Default Supplier", "default@supplier.com")

        normalized = product_type.strip().lower()
        if normalized == "physical":
            return PhysicalProduct(product_id, name, price, stock, extra_value, supplier)
        elif normalized == "digital":
            return DigitalProduct(product_id, name, price, stock, extra_value, supplier)
        else:
            raise ValueError(f"Unknown product type: {product_type}")