#!/usr/bin/python3
"""this module define a class Square that inherits from Rectangle:"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a Square class hat inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialize a new square

        Args:
            size (int): the square height and widtg
            x (int): the position coordinate of x
            y (int): the position coordinate of y
            id (int): the id of the suqare

        """
        super().__init__(size, size, x, y, id)
