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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """int: get and set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: get and set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """int: get and set the x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """int: get and set the y position of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area value of
        the Rectangle instance"""
        return (self.width * self.height)

    def display(self):
        """public method that prints in stdout the Rectangle instance
        with the character #"""
        if (self.width == 0 and self.height == 0):
            print()
        else:
            for y in range(self.y):
                print()
            for i in range(self.height):
                for x in range(self.x):
                    print(" ", end="")
                print("#" * self.width, end="")
                print()

    def __str__(self):
        """overriding the __str__ method"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """public method that assigns an argument to each attribute

        Args:
            *args (int):
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        **kwargs (int): assigns a key/value argument to attributes

        """
        if (len(args) != 0 and not (args in None)):
            attr_len = len(args)
            if attr_len >= 1:
                self.id = args[0]
            if attr_len >= 2:
                self.width = args[1]
            if attr_len >= 3:
                self.height = args[2]
            if attr_len >= 4:
                self.x = args[3]
            if attr_len >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
