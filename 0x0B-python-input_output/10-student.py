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

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation of
        a Student instance
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved

        Args:
            attrs (list , optional): attribut to retrieve

        """
        if (attrs is not None and type(attrs) is list
                and all(type(i) is str for i in attrs)):
            op_ret = dict()
            for j in attrs:
                if hasattr(self, j):
                    op_ret.update({j: getattr(self, j)})
            return dict(sorted(op_ret.items()))
        return (self.__dict__)
