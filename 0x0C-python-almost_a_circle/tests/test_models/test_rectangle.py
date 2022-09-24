#!/usr/bin/python3
"""this module contains unit tests for the rectangle module"""
import unittest
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """this is a unittest class"""
    
    def test_for_module_documentation(self):
        """you gotta have docs"""
        self.assertTrue(len(rectangle.__doc__) > 0)

    def test_for_class_documentation(self):
        """you gotta have docs"""
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_for_init_documentation(self):
        """you gotta have docs"""
        self.assertTrue(len(Rectangle.__init__.__doc__) > 0)

    def test_rec_id(self):
        """test giving rectangle an id"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1)
        r2 = Rectangle(2, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        
if __name__ == "__main__":
    unittest.main()
