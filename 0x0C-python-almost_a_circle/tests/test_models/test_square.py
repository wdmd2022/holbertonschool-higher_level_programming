#!/usr/bin/python3
"""this module contains unit tests for the square module"""
import unittest
from models.square import Square

class CheckSomething(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()
# ENDIF
