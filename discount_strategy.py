from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float) -> None:
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100.")
        self._percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self._percentage / 100.0)

class BulkDiscount(DiscountStrategy):
    def __init__(self, threshold: float, amount: float) -> None:
        if threshold < 0 or amount < 0:
            raise ValueError("Threshold and discount amount must be non-negative.")
        self._threshold: float = threshold
        self._amount: float = amount

    def apply(self, total: float) -> float:
        if total >= self._threshold:
            return max(0.0, total - self._amount)
        return total

class StudentDiscount(DiscountStrategy):
    def __init__(self, percentage: float = 5.0) -> None:
        self._percentage: float = percentage

    def apply(self, total: float) -> float:
        return total * (1 - self._percentage / 100.0)