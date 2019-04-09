# Matthew Jones
# CPE 202-01
# 4/5/19

import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr1(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_repr2(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertNotEqual(repr(loc),"Location('SLO', 35.3, 120.7)")

    def test_repr3(self):
        loc = Location("Paris", 48.9, 2.4)
        self.assertEqual(repr(loc),"Location('Paris', 48.9, 2.4)")

    def test_eq1(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 =Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1==loc2)

    def test_eq2(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = loc1
        self.assertTrue(loc1==loc2)

    def test_eq3(self):
        loc1 = Location("SLO", 35.3, -120.7)
        loc2 = Location("LA", 34.1, 118.2)
        self.assertFalse(loc1 == loc2)

if __name__ == "__main__":
        unittest.main()
