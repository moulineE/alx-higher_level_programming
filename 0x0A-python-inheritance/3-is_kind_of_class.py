#!/usr/bin/python3
"""This modules define a class that verify if an object is an
instance or an inherited instance of the specified class"""


def is_kind_of_class(obj, a_class):
    """ verify if the object is an
instance or an inherited instance of the specified class

    Args:
        obj (any): the object to verify
        a_class (type): the correct class

    Return:
        if the object is an instance or inhertited instance of
    the specified class "a_class": True
        else: False

    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
