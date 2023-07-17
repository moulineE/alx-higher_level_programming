#!/usr/bin/python3
"""This module define a "Base" class"""


class Base:
    """a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor

        Args:
            id (int): the id of the new base instance

        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
