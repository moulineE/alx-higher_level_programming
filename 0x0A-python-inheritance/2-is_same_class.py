#!/usr/bin/python3
"""This modules define a class that verify if an object is an
instance of the specified class"""


def is_same_class(obj, a_class):
    """ verify if the object is exactly an instance of
    the specified class

    Args:
        obj (any): the object to verify
        a_class (type): the correct class

    Return:
        if the object is exactly an instance of
    the specified class "a_class": True
        else: False

    """
    if type(obj) is a_class:
        return True
    else:
        return False
