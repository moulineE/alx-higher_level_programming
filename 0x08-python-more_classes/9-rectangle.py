#!/usr/bin/python3
"""eclass Rectangle that defines a rectangle"""


class Rectangle:
    """rectangle class

    Attributes:
        number_of_instances (int): number of instance of rectangle
        print_symbol (str): the simbole used to represent the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

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
                rec_repr.append(str(self.print_symbol) * self.__width)
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): an instance of rectangle to compare
            rect_2 (Rectangle): an instance of rectangle to compare
        Raises:
            TypeError: raise a TypeError exception with the message
            must be an instance of Rectangle if rect_1 or rect_2 is
            not a rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size

        Args:
            size (int): the size of the square
        """
        return cls(size, size)
