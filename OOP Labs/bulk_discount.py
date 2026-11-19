from discount_strategy import DiscountStrategy

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        if threshold < 0 or amount < 0:
            raise ValueError("Threshold and amount must be non-negative.")
        self._threshold: float = threshold
        self._amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return max(0.0, total - self._amount)
        return total