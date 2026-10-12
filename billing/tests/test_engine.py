import sys, unittest
sys.path.insert(0, '.')
from billing.engine import calculate_pizza_price, calculate_subtotal, calculate_tax, receipt_text

class TestBillingEngine(unittest.TestCase):
    def test_small_with_basic(self):
        self.assertEqual(calculate_pizza_price("Small", ["Cheese", "Pepperoni"]), 12.0)
    def test_large_with_deluxe(self):
        self.assertEqual(calculate_pizza_price("Large", ["Sausage", "Feta Cheese"]), 24.0)
    def test_tax_rounded_up(self):
        self.assertEqual(calculate_tax(10.0), 0.5)
        self.assertEqual(calculate_tax(10.01), 0.51)
    def test_receipt_format(self):
        items = [{"size":"Medium","toppings":["Ham"],"price":16.0}]
        r = receipt_text(items)
        self.assertIn("Subtotal:", r)
        self.assertIn("TAX", r)

if __name__ == "__main__":
    unittest.main(verbosity=2)
