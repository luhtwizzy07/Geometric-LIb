import unittest

from triangle import triangle_area
from triangle import triangle_perimeter

class TriandleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = triangle_area(0, 10)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = triangle_perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_valid_area(self):
        res = triangle_area(3,2)
        self.assertEqual(res, 3)

    def test_valid_perimeter(self):
        res = triangle_perimeter(3, 2, 4)
        self.assertEqual(res, 9)

    def test_negative_area(self):
        res = triangle_area(-10,-1)
        self.assertFalse

    def test_negative_perimeter(self):
        res = triangle_perimeter(-2, 4, 8)
        self.assertFalse

    def invalid_triangle_perimeter(self):
        res = triangle_perimeter(10, 3, 2)
        self.assertFalse