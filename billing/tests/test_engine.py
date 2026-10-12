import unittest
import sys
sys.path.insert(0, '.')
from billing.engine import receipt_text

class TestBillingEngine(unittest.TestCase):
    def test_receipt_external_behavior(self):
        items = [{"size":"Medium","toppings":["Ham"],"price":16.0}]
        r = receipt_text(items)
        self.assertIn("Subtotal: 16.00", r)
        self.assertIn("TAX (5%): 0.80", r)  # 16 * 0.05 = 0.8
        self.assertIn("Total: 16.80", r)

    def test_receipt_multiple_items(self):
        items = [
            {"size":"Small","toppings":["Cheese"],"price":11.0},
            {"size":"Large","toppings":["Sausage","Olives"],"price":24.0},
        ]
        r = receipt_text(items)
        self.assertIn("Subtotal: 35.00", r)
        # tax on 35 = ceil(1.75*100)/100 = 1.75; total 36.75
        self.assertIn("Total: 36.75", r)

if __name__ == "__main__":
    unittest.main(verbosity=2)
