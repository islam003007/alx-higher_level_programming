#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit test for max_intger([..])"""
    
    def test_normal_list(self):
        """tests normal condition"""
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)
    
    def test_missing_argument(self):
        """tests missing one argument"""
        self.assertIsNone(max_integer())
    
    def test_type_error(self):
        """tests typeError condition"""
        list = 5
        self.assertRaises(TypeError, max_integer, list)
    
    def test_negative_list(self):
        """tests negative list condition"""
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)
    
    def test_str(self):
        """tests str condition"""
        list = "asd"
        self.assertEqual(max_integer(list), "s")
    
    def test_dictionary(self):
        """tests dictionary"""
        dic = {"ahmed": 5, "ashraf": 6, "islam": 3}
        self.assertRaises(KeyError, max_integer, dic)


if __name__ == "__main__":
    import unittest
    unittest.main()
