#!/usr/bin/python3
"""this module contains unit tests for the base module"""
import unittest
from models import base
from models.base import Base

class TestBase(unittest.TestCase):
    """this is a unittest class"""

    def test_for_module_documentation(self):
        """you gotta have docs"""
        self.assertTrue(len(base.__doc__) > 0)

    def test_for_class_documentation(self):
        """even for the class"""
        self.assertTrue(len(Base.__doc__) > 0)

    def test_for_init_documentation(self):
        """and docs for the init function"""
        self.assertTrue(len(Base.__init__.__doc__) > 0)
    
    def test_base_id(self):
        """test giving base an id"""
        b1 = Base(2)
        self.assertEqual(b1.id, 2)

if __name__ == "__main__":
    unittest.main()
