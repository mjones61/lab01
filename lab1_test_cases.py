# Matthew Jones
# CPE 202-01
# 4/5/19

import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max1(self):
        # tests list is None functionality
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max2(self):
        # tests list is empty functionality
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

    def test_max3(self):
        # tests maximum finding for nonempty list
        tlist = [12, 4, 6, 8, 15]
        self.assertEqual(max_list_iter(tlist), 15)

    def test_reverse1(self):
        # tests reversal of list with length 3
        self.assertEqual(reverse_rec([1,2,3]), [3,2,1])

    def test_reverse2(self):
        # tests reversal of list with length 0
        self.assertEqual(reverse_rec([]), [])

    def test_reverse3(self):
        # tests list is None functionality
        lst = None
        with self.assertRaises(ValueError):
            reverse_rec(lst)

    def test_bin1(self):
        # tests binary search with target in the middle of the list
        list_val = [0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)

    def test_bin2(self):
        # tests binary search with target at end of the list
        list_val = [0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)

    def test_bin3(self):
        # tests binary search with target at beginning of the list
        list_val = [0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)

    def test_bin4(self):
        # tests list is empty functionality
        list_val = []
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), None)

    def test_bin5(self):
        # tests list is None functionality
        list_val = None
        with self.assertRaises(ValueError):
            bin_search(4, 0, 10, list_val)

    def test_bin6(self):
        # tests list is None functionality
        list_val = [0,1,2,3,4,7,8,9,10]
        with self.assertRaises(ValueError):
            bin_search(4, 5, 2,list_val)

    def test_bin7(self):
        # tests list is None functionality
        list_val = [0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(5, 0, len(list_val) - 1, list_val), None)

if __name__ == "__main__":
        unittest.main()

    
