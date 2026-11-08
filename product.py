from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier) -> None:
        self._product_id: str = product_id
        self._name: str = name
        self._price: float = price
        self._stock: int = stock
        self._supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self._product_id
    
    def get_name(self) -> str:
        return self._name
    
    def get_price(self) -> float:
        return self._price
    
    def get_stock(self) -> int:
        return self._stock

    def get_supplier(self) -> Supplier:
        return self._supplier
        
    def update_stock(self, quantity: int) -> None:
        if quantity >= 0:
            self._stock = quantity

    def display_information(self) -> None:
        print(f"ID: {self._product_id} | Name: {self._name} | Price: ${self._price:.2f} | Stock: {self._stock}", end="")

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        """Return delivery/fulfilment information for this product type."""
        pass

    # def copy(self):
    #     return self.__class__(self.__product_id, self.__name, self.__price, self.__stock)