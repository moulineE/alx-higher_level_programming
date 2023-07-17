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

    @property
    def size(self):
        """int: get and set the size of the rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """overriding the __str__ method"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """public method that assigns attributes:

        Args:
            *args (int):  is the list of arguments - no-keyworded arguments
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
            **kwargs (int): assigns a key/value argument to attributes

        """
        if (len(args) != 0 and args):
            attr_len = len(args)
            if attr_len >= 1:
                self.id = args[0]
            if attr_len >= 2:
                self.width = args[1]
            if attr_len >= 3:
                self.x = args[2]
            if attr_len >= 4:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """public method that returns the dictionary representation
        of a Square"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
