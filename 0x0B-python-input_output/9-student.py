#!/usr/bin/python3
"""this module contains a class Student"""


class Student(first_name, last_name, age):
    """this class represents a Student object"""
    def __init__(self, first_name, last_name, age):
        """initializes the Student"""
        Student.first_name = first_name
        Student.last_name = last_name
        Student.age = age
    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return Student.__dict__
