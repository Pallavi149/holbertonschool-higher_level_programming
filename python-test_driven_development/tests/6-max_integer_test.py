#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertTrue(max_integer([]) is None)

    def test_no_arg(self):
        self.assertTrue(max_integer() is None)

    def test_none_arg(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_last_max(self):
        self.assertEqual(max_integer([1, 4, 6, 9, 12]), 12)

    def test_first_max(self):
        self.assertEqual(max_integer([13, 4, 6, 9, 12]), 13)

    def test_float_max(self):
        self.assertEqual(max_integer([1, 44.4, 6, 9, 12]), 44.4)

    def test_one_item_list(self):
        self.assertEqual(max_integer([12]), 12)

    def test_negative_item(self):
        self.assertEqual(max_integer([1, -44.4, 6, 9, 12]), 12)

    def test_all_negative(self):
        self.assertEqual(max_integer([-1, -44.4, -6, -9, -12]), -1)

    def test_float_inf(self):
        self.assertEqual(max_integer([1, 44.4, 6, 9, 12,
                                      float('inf')]), float("inf"))
    def test_float_nan(self):
        self.assertEqual(max_integer([1, 44.4, 6, 9, float('NaN')]), 44.4)

    def test_string_list(self):
        self.assertEqual(max_integer(["1", "3", "test"]), "test")

    def test_mixed_list(self):
        with self.assertRaises(TypeError):
            max_integer([1, 3, "test"])
