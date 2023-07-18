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

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of
        list_objs to a file:

        Args:
            list_objs (lsit): a list of instances who inherits of Base

        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write([])
            else:
                list_str = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(list_str))

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the JSON string
        representation json_string

        Args:
            json_string (str): a string representing a list of dictionaries
        Returns:
            return the list represented by json_string

        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
