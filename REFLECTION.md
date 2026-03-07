# Project Reflection & SOLID Principles

## 1. SOLID Principles Applied
I strictly applied the **Open/Closed Principle (OCP)** using the Strategy Pattern. By creating an Abstract Base Class (`PricingStrategy`), the system is open for extension (I can add a new `HolidayDiscount` class anytime) but closed for modification (I don't have to change the core `ShoppingCart` code to do it).

## 2. Which OOP Concept was the Hardest?
**Dependency Injection** felt strange at first—passing a class (like `PercentageDiscount`) into the constructor of another class (`ShoppingCart`). However, once I saw how it allowed the cart to calculate totals dynamically without needing massive `if/else` statements for every discount type, the power of Abstraction clicked for me.

## 3. What Design Mistakes Did I Make Initially?
I initially tried to build inheritance directly into the products (e.g., `DiscountedProduct`), but I realized this violated **Composition over Inheritance**. A cart *has* items, and a cart *uses* a pricing strategy. Separating these concepts made the cart much more flexible.

## 4. What Would I Improve?
I would expand the data models to include complex scenarios like inventory tracking (so users can't add items to the cart that are out of stock) and adding tax/shipping calculation strategies alongside the discount strategies.