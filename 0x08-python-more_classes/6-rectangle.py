#!/usr/bin/python3
"""eclass Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle class

    Attributes:
        number_of_instances (int): number of instance of rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initionlize a new rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get the reactangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the reactangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Public instance method that returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method that returns the rectangle perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """print the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            rec_repr = []
            for i in range(self.__height):
                rec_repr.append("#" * self.__width)
                if i != self.__height - 1:
                    rec_repr.append("\n")
        return (''.join(rec_repr))

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance"""
        return ('Rectangle(' + str(self.__width) + ','
                + " " + str(self.__height) + ')')

    def __del__(self):
        """Print the message 'Bye rectangle...'
        when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
