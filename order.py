from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self._order_id: str = order_id
        self._order_lines: list[OrderLine] = [] 

    def get_order_id(self) -> str:
        return self._order_id

    def add_order_line(self, product: Product, quantity: int) -> None:
        line = OrderLine(product, quantity)
        self._order_lines.append(line)

    def remove_order_line(self, index: int) -> None:
        if 0 <= index < len(self._order_lines):
            self._order_lines.pop(index)

    def get_order_lines(self) -> tuple:
        return tuple(
            (line.get_product(), line.get_quantity(), line.calculate_subtotal()) 
            for line in self._order_lines
        )

    def calculate_total(self) -> float:
        total: float = 0.0
        for line in self._order_lines:
            total += line.calculate_subtotal()
        return total