#!/usr/bin/python3
"""this module define the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize a new rectangle

        Args:
            width (int): is the width of rectangle
            height (int): is the height of the rectangle
            x (int): the position of the triangle
            y (int): the position of the triangle
            id (int) the id of the triangle

        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """int: get and set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """int: get and set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """int: get and set the x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value
        
    @property
    def y(self):
        """int: get and set the y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
