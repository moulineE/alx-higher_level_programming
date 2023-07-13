#!/usr/bin/python3
"""this module define a class MyInt that inherits from int"""


class MyInt(int):
    """class that invert the operator '==' and '!='"""

    def __eq__(self, value):
        """invert the '==' operator"""
        return int != value

    def __ne__(self, value):
        """invert the '!=' operator"""
        return int == value
