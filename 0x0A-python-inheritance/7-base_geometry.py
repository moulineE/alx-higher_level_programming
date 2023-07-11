#!/usr/bin/python3
"""this module define a BaseGeometriy class in dev"""


class BaseGeometry:
    """a class BaseGeometry that is a placeholder"""

    def area(self):
        """that raises an Exception because not implemented

        Raises:
            Exception: area() is not implemented

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validate the type and value range of 'value'

        Args:
             name (str): the name of the value
             value (int): the value
        Raises:
            TypeError: <name> must be an integer if value is not an int
            ValueError: <name> must be greater than 0 if value <= 0

        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
