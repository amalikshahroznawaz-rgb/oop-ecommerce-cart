from typing import Dict, List
from .models import CartItem, Product, PricingStrategy

class ShoppingCart:
    def __init__(self, strategy: PricingStrategy):
        self._items: Dict[str, CartItem] = {}
        self.strategy = strategy

    def add(self, product: Product, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("Quantity must be at least 1.")
        
        # If product already in cart, just increase quantity
        if product.sku in self._items:
            self._items[product.sku].qty += qty
        else:
            self._items[product.sku] = CartItem(product, qty)

    def remove(self, sku: str) -> None:
        if sku not in self._items:
            raise KeyError(f"Product with SKU '{sku}' not found in cart.")
        del self._items[sku]

    def subtotal(self) -> float:
        # Sum of all individual item subtotals
        return sum(item.subtotal() for item in self._items.values())

    def total(self) -> float:
        # Apply the injected pricing strategy to the subtotal
        return self.strategy.calculate(self.subtotal())
    
    def get_items(self) -> List[CartItem]:
        return list(self._items.values())