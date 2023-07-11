#!/usr/bin/python3
"""This modules define a class that verify if an object is an instance of a
class that inherited (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """ verify if the object is a subclass of the specified class

    Args:
        obj (any): the object to verify
        a_class (type): the correct class

    Return:
        if the object is a subclass ofthe specified class
        "a_class": True
        else: False

    """
    if (issubclass(type(obj), a_class) and type(obj) is not a_class):
        return True
    else:
        return False
