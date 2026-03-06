from src.models import Product, NoDiscount, PercentageDiscount
from src.cart import ShoppingCart

def main():
    # Pre-populate a fake "database" of products
    store_products = {
        "1": Product("1", "Mechanical Keyboard", 120.0),
        "2": Product("2", "Gaming Mouse", 60.0),
        "3": Product("3", "Monitor", 300.0)
    }

    # Ask user to pick a pricing strategy upfront
    print("Welcome to the Store!")
    print("1. Standard Pricing")
    print("2. VIP Member (20% Discount)")
    strat_choice = input("Select pricing tier: ")
    
    if strat_choice == '2':
        cart = ShoppingCart(PercentageDiscount(20.0))
        print("VIP Discount Applied!")
    else:
        cart = ShoppingCart(NoDiscount())
        print("Standard Pricing Applied.")

    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. View Store Products")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart & Checkout")
        print("5. Exit")
        
        choice = input("Enter choice: ")

        try:
            if choice == '1':
                print("\n--- Available Products ---")
                for p in store_products.values():
                    print(f"SKU: {p.sku} | {p.name} - ${p.price:.2f}")

            elif choice == '2':
                sku = input("Enter SKU to add: ")
                if sku not in store_products:
                    print("ERROR: Product not found.")
                    continue
                qty = int(input("Enter quantity: "))
                cart.add(store_products[sku], qty)
                print(f"Success: Added to cart.")

            elif choice == '3':
                sku = input("Enter SKU to remove: ")
                cart.remove(sku)
                print("Success: Item removed.")

            elif choice == '4':
                items = cart.get_items()
                if not items:
                    print("Cart is empty.")
                    continue
                
                print("\n--- Your Receipt ---")
                for item in items:
                    print(f"{item.product.name} x{item.qty} = ${item.subtotal():.2f}")
                print("-" * 20)
                print(f"Subtotal: ${cart.subtotal():.2f}")
                print(f"Total (After Discount): ${cart.total():.2f}")
                print("Thank you for your purchase!")
                break

            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice.")

        except (ValueError, KeyError) as e:
            print(f"ERROR: {e}")

if __name__ == "__main__":
    main()