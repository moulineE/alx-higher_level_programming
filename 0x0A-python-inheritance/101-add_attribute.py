#!/usr/bin/python3
"""This module define a function that adds a new attribute to an object
if it’s possible"""


def add_attribute(obj, attr_name, attr_value):
    """a function that adds a new attribute to an object if it’s possible

    Args:
        obj (any): the object to add atribut to
        attr_name (str): the name of the new attrtibut
        attr_value (str): the value of the new attribue

    Raises:
        TypeError: "can't add new attribute" id the object can’t have
        new attribute

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        return setattr(obj, attr_name, attr_value)
