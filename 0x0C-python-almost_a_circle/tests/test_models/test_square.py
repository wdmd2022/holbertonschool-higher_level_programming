#!/usr/bin/python3
"""this module contains unit tests for the square module"""
import unittest
from models import square
from models.square import Square

class TestSquare(unittest.TestCase):
    """this is a unittest class"""
    
    def test_for_module_documentation(self):
        """you gotta have docs"""
        self.assertTrue(len(square.__doc__) > 0)

    def test_for_class_documentation(self):
        """"class docs too"""
        self.assertTrue(len(Square.__doc__) > 0)

    def test_for_init_documentation(self):
        """even for init"""
        self.assertTrue(len(Square.__init__.__doc__) > 0)

    def test_square_id(self):
        """test giving square an id"""
        s1 = Square(1)
        s2 = Square(2)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)

    def test_square_size(self):
        """test giving square a size"""
        s1 = Square(1)
        s2 = Square(2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s2.size, 2)
        
if __name__ == "__main__":
    unittest.main()
