# E-Commerce Cart System

A robust Shopping Cart backend demonstrating the Strategy Pattern and Composition.

## OOP Concepts Used
* **Abstraction & Polymorphism**: `PricingStrategy` allows the cart to calculate totals dynamically without knowing the specific discount rules.
* **Composition**: `ShoppingCart` manages multiple `CartItem` objects, which in turn contain `Product` objects.
* **Open/Closed Principle**: New discount types can be added simply by creating a new class that inherits from `PricingStrategy`, without changing the cart's code.

## Running the CLI
python cli.py

## Running the Tests
python -m unittest tests/test_cart.py
## Assumptions Made
* All product quantities added to the cart must be integers greater than zero.
* The Shopping Cart accepts a single PricingStrategy at initialization, which applies to the entire subtotal.
* The system does not currently handle tax or shipping calculations, only base product prices and discounts.