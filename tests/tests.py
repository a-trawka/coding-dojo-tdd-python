import unittest
from dojo import price


class BasketTest(unittest.TestCase):
    def test_empty_basket(self):
        self.assertEqual(0, price([]))

    def test_basket_with_one_book(self):
        self.assertEqual(8, price([0]))

    def test_price_with_two_distinct_books(self):
        self.assertEqual((8 * 2 * 0.95), price([0, 1]))

    def test_price_with_two_same_books(self):
        self.assertEqual((8 * 2), price([0, 0]))

    def test_price_with_two_same_and_one_diff_book(self):
        self.assertEqual((8 * 2 * 0.95)+8, price([0, 0, 1]))

    def test_price_with_two_sets_of_books(self):
        self.assertEqual((8 * 4 * 0.8)+(8 * 2 * 0.95), price([0, 0, 1, 2, 2, 4]))
        self.assertEqual((8 * 4 * 0.8)+(8 * 2 * 0.95), price([0, 3, 1, 3, 4, 0]))
