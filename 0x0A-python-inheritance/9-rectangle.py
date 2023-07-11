#!/usr/bin/python3
"""This module define a class Rectangle  that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class is a subclass that represent a rectangle"""

    def __init__(self, width, height):
        """initialize a new rectangle

        Args:
            width (int) must be a private and positif integer
            height (int) must be a private and positif integer

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This methode return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return, the following rectangle description:
        [Rectangle] <width>/<height>"""
        return "[{}] {}/{}".format(type(self).__name__, self.__width,
                                   self.__height)
