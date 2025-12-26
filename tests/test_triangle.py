import unittest

from triangle import area
from triangle import perimeter

class TriandleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_area1(self):
        res = area(3, 2)
        self.assertEqual(res, 3)

    def test_perimeter1(self):
        res = perimeter(3, 2, 4)
        self.assertEqual(res, 9)

    def test_area2(self):
        res = area(3.22, 10)
        self.assertEqual(res, 16.1)

    def test_perimeter2(self):
        res = perimeter(3.22, 5, 6.808)
        self.assertEqual(res, 15.028)