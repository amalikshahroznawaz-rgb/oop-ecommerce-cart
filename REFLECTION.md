# Project Reflection & SOLID Principles

## 1. SOLID Principles Applied
Throughout these projects, I made a conscious effort to apply the SOLID principles of object-oriented design:
* **Single Responsibility Principle (SRP):** I strictly separated the user interface from the business logic. The `cli.py` file handles all the `print()` and `input()` statements, while the `models.py` and `services.py` files only handle data and rules. This makes the code much easier to test.
* **Open/Closed Principle (OCP):** In the E-commerce Cart (and the Library Fine System), I used the Strategy Pattern. By creating an Abstract Base Class (`PricingStrategy`), the system is open for extension (I can add a new `HolidayDiscount` class anytime) but closed for modification (I don't have to change the core `ShoppingCart` code to do it).
* **Liskov Substitution Principle (LSP):** In the Banking System, the `Bank` class expects base `Account` objects. Because `SavingsAccount` and `CurrentAccount` strictly follow the contract of the base `Account` class (even though they override `withdraw()`), the system works flawlessly without needing to know which specific account type it is dealing with.

## 2. Which OOP Concept was the Hardest?
The hardest concept to grasp initially was **Polymorphism combined with Dependency Injection** (specifically the Strategy Pattern). It felt strange at first to pass a class (like `PercentageDiscount`) into the constructor of another class (`ShoppingCart`). However, once I saw how it allowed the cart to calculate totals without needing massive `if/else` statements for every discount type, the power of Abstraction clicked for me.

## 3. What Design Mistakes Did I Make Initially?
My biggest initial mistake was the temptation to put `print()` statements directly inside my business logic classes (for example, printing "Not enough funds!" inside the `withdraw` method). I quickly realized that doing this tightly couples the UI to the backend, making it absolutely impossible to write automated Unit Tests. I refactored the code to `raise ValueError` instead, allowing the `cli.py` to catch the error and print it nicely.

## 4. What Would I Improve?
If I were to expand this software into a production environment, I would improve the data persistence. Currently, everything is stored in in-memory dictionaries (like `self.accounts = {}`), meaning all data is lost when the program closes. I would improve this by integrating an SQLite database or saving the state to JSON files using Python's `json` module. Additionally, I would add a proper logging mechanism using Python's `logging` library instead of just printing to the console.