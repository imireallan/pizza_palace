# E2E billing flow (ticket 03) — red
import unittest, sys, json
sys.path.insert(0, '.')
from billing.engine import calculate_pizza_price, receipt_text, calculate_tax

class TestE2EFlow(unittest.TestCase):
    def test_unknown_size_rejected(self):
        with self.assertRaises(ValueError) as cm:
            calculate_pizza_price("Huge", ["Cheese"])
        self.assertIn("Unknown size", str(cm.exception))

    def test_receipt_from_payload(self):
        # Integration seam: payload -> receipt
        items = [{"size":"Medium","toppings":["Ham","Sausage"],"price":18.0}]
        r = receipt_text(items)
        self.assertIn("Subtotal:", r)
        self.assertIn("TAX (5%):", r)
        self.assertIn("Total:", r)

if __name__ == "__main__":
    unittest.main(verbosity=2)
