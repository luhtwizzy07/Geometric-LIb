import unittest

from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0 )

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_area1(self):
        res = area(2, 3)
        self.assertEqual(res, 6)

    def test_perimeter1(self):
        res = perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_area2(self):
        res = area(3.41, 14)
        self.assertEqual(res, 47.74)

    def test_perimeter2(self):
        res = perimeter(3.41, 14)
        self.assertEqual(res, 34.82)