#!/usr/bin/python3
"""This module define a fonction
that add two integre with the second
is by default 98
a and b must be integers or floats
"""


def add_integer(a, b=98):
    """a function that adds 2 integers

    Args:
        a (int, float): the fist digit to add
        b (int, float): the second digit to add

    Returns:
        int:
            a + b

    Raises:
        TypeError: if a and b are not an integers or floats
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
