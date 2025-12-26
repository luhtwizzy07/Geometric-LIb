import unittest

from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res,0)

    def test_valid_area(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_valid_perimeter(self):
        res = perimeter(2)
        self.assertEqual(res, 12.566370614359172)

    def test_negative_area(self):
        res = area(-10)
        self.assertFalse

    def test_negative_perimeter(self):
        res = perimeter(-2)
        self.assertFalse
