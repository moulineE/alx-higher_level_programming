#!/usr/bin/python3
"""This module define a class Square  that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class is a subclass that represent a square"""

    def __init__(self, size):
        """initialize a new square

        Args:
            size (int) must be a private and positif integer

        """
        super().__init__(size, size)
        self.__size = size
