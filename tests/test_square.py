import unittest

from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_area1(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_perimeter1(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_area2(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter2(self):
        res = perimeter(10)
        self.assertEqual(res, 40)