#!/usr/bin/python3
"""this module define a class Student that defines a student"""


class Student:
    """class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new instance of student

        Args:
            first_name (str): the student first name
            last_name (str): the student last name
            age (int): the student age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves a dictionary representation of
        a Student instance"""
        return self.__dict__
