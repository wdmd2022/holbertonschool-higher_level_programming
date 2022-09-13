#!/usr/bin/python3
"""Unit test for max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unit test for max integer function"""

    def testempty(self):
        """for when there is nothing in the list"""
        uselesslist = []
        self.assertIsNone(max_integer(uselesslist))

    def testnoargument(self):
        """for when there is no argument passed"""
        self.assertIsNone(max_integer())

    def orderedlist(self):
        """for when the biggest is last"""
        ordered = [1, 2, 3]
        self.assertEqual(max_integer(ordered), 3)

    def unorderedlist(self):
        """for when the biggest is not first or last"""
        unordered = [2, 7, 1]
        self.assertEqual(max_integer(unordered), 7)

    def floatyboy(self):
        """for an unordered list of floats"""
        floaton = [45.7, 655.901, 7.0]
        self.assertEqual(max_integer(floaton), 655.901)

    def getnegative(self):
        """for when things are all negative"""
        sadlist = [-1, -3, -799]
        self.assertEqual(max_integer(sadlist), -1)

if __name__ == '__main__':
    unittest.main()
