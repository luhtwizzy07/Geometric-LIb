import unittest

from rectangle import rectangle_area
from rectangle import rectangle_perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle_area(10,0)
        self.assertEqual(res, 0 )

    def test_zero_perimeter(self):
        res = rectangle_perimeter(0,0)
        self.assertEqual(res, 0)

    def test_valid_area(self):
        res = rectangle_area(2,3)
        self.assertEqual(res, 6)

    def test_valid_perimeter(self):
        res = rectangle_perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_negative_area(self):
        res = rectangle_area(-10,-1)
        self.assertFalse

    def test_negative_perimeter(self):
        res = rectangle_perimeter(-2, 4)
        self.assertFalse