import unittest

from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_area1(self):
        res = area(2)
        self.assertEqual(res, 12.566370614359172)

    def test_perimeter1(self):
        res = perimeter(2)
        self.assertEqual(res, 12.566370614359172)

    def test_area2(self):
        res = area(7.77)
        self.assertEqual(res, 189.6670591159112)

    def test_perimeter2(self):
        res = perimeter(7.77)
        self.assertEqual(res, 48.82034983678538)
