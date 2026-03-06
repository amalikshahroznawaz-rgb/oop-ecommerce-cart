from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

# --- Pricing Strategies (Abstraction & Polymorphism) ---
class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, subtotal: float) -> float:
        pass

class NoDiscount(PricingStrategy):
    def calculate(self, subtotal: float) -> float:
        return subtotal

class PercentageDiscount(PricingStrategy):
    def __init__(self, percent: float):
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def calculate(self, subtotal: float) -> float:
        return subtotal * (1 - self.percent / 100)

# --- Data Models (Composition) ---
@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    price: float

@dataclass
class CartItem:
    product: Product
    qty: int = 1

    def subtotal(self) -> float:
        return self.product.price * self.qty