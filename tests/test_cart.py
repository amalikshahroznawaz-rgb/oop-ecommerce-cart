import unittest
from src.models import Product, NoDiscount, PercentageDiscount
from src.cart import ShoppingCart

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.p1 = Product("P1", "Laptop", 1000.0)
        self.p2 = Product("P2", "Mouse", 50.0)
        self.cart_no_discount = ShoppingCart(NoDiscount())
        self.cart_discount = ShoppingCart(PercentageDiscount(10.0)) # 10% off

    def test_1_add_product_creates_item(self):
        self.cart_no_discount.add(self.p1, 1)
        self.assertEqual(len(self.cart_no_discount.get_items()), 1)
        self.assertEqual(self.cart_no_discount.subtotal(), 1000.0)

    def test_2_add_existing_product_increases_qty(self):
        self.cart_no_discount.add(self.p1, 1)
        self.cart_no_discount.add(self.p1, 2)
        items = self.cart_no_discount.get_items()
        self.assertEqual(items[0].qty, 3)
        self.assertEqual(self.cart_no_discount.subtotal(), 3000.0)

    def test_3_add_invalid_qty_fails(self):
        with self.assertRaises(ValueError):
            self.cart_no_discount.add(self.p1, 0)

    def test_4_remove_product_success(self):
        self.cart_no_discount.add(self.p1, 1)
        self.cart_no_discount.remove("P1")
        self.assertEqual(len(self.cart_no_discount.get_items()), 0)

    def test_5_remove_nonexistent_product_fails(self):
        with self.assertRaises(KeyError):
            self.cart_no_discount.remove("P99")

    def test_6_no_discount_total_equals_subtotal(self):
        self.cart_no_discount.add(self.p1, 1) # $1000
        self.cart_no_discount.add(self.p2, 2) # $100
        self.assertEqual(self.cart_no_discount.subtotal(), 1100.0)
        self.assertEqual(self.cart_no_discount.total(), 1100.0)

    def test_7_percentage_discount_applied_correctly(self):
        self.cart_discount.add(self.p1, 1) # $1000
        self.cart_discount.add(self.p2, 2) # $100
        self.assertEqual(self.cart_discount.subtotal(), 1100.0)
        self.assertEqual(self.cart_discount.total(), 990.0) # 10% off 1100

    def test_8_invalid_percentage_discount_fails(self):
        with self.assertRaises(ValueError):
            PercentageDiscount(150.0) # Cannot be over 100%

if __name__ == '__main__':
    unittest.main()