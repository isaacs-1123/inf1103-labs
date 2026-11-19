from discount_strategy import DiscountStrategy

class StudentDiscount(DiscountStrategy):
    def __init__(self, percent: float = 5.0) -> None:
        self._percent: float = percent

    def apply(self, total: float) -> float:
        return total * (1 - self._percent / 100.0)