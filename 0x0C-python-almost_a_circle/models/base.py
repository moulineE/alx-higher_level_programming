#!/usr/bin/python3
"""This module define a "Base" class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method  that returns the JSON string representation
        of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries
        Returns:
            the JSON string representation of list_dictionaries

        """
        if list_dictionaries is None or list_dictionaries is []:
            return []
        else:
            return json.dumps(list_dictionaries)
