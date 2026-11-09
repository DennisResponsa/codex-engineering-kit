"""Public, entirely synthetic acceptance cases for the order demo."""
import unittest
from app import quote


class QuoteTests(unittest.TestCase):
    def test_discount_excludes_shipping(self):
        self.assertEqual(quote([(1000, 2)], 500, 10), 2300)

    def test_full_discount_keeps_shipping(self):
        self.assertEqual(quote([(1000, 2)], 500, 100), 500)

    def test_no_discount(self):
        self.assertEqual(quote([(1250, 2), (300, 1)], 500, 0), 3300)

    def test_half_cent_rounds_up(self):
        self.assertEqual(quote([(101, 1)], 0, 50), 51)

    def test_free_shipping(self):
        self.assertEqual(quote([(2000, 1)], 0, 10), 1800)

    def test_invalid_discount(self):
        for value in (-1, 101, True, 2.5):
            with self.subTest(value=value), self.assertRaises(ValueError):
                quote([(1000, 1)], 0, value)

    def test_invalid_price_or_quantity(self):
        for item in ((-1, 1), (100, 0), (100, -1), (True, 1), (100, 1.5)):
            with self.subTest(item=item), self.assertRaises(ValueError):
                quote([item], 0, 0)

    def test_invalid_shipping_or_empty_cart(self):
        for value in (-1, True, 0.5):
            with self.subTest(value=value), self.assertRaises(ValueError):
                quote([(100, 1)], value, 0)
        with self.assertRaises(ValueError):
            quote([], 0, 0)


if __name__ == '__main__':
    unittest.main()
