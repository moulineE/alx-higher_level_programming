#!/usr/bin/python3
"""This module define a "Base" class"""
import json
import csv
import turtle


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
            return "[]"
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
                f.write("[]")
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

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with
        all attributes already set

        Args:
            **dictionary (dict): can be thought of as a double pointer
            to a dictionary

        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            elif cls.__name__ == "Square":
                new = cls(1)
            else:
                new = None
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances from a file

        Returns:
                return a list of instances

        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                return [cls.create(**dct) for dct in
                        Base.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """class method that writes the csv representation of
        list_objs to a file:

        Args:
            list_objs (lsit): a list of instances of Base

        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline='') as csvfile:
            if list_objs is None or list_objs is []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            for i in list_objs:
                writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """class method that returns a list of instances from a file

        Returns:
                return a list of instances

        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline='') as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(csvfile, fieldnames=fieldnames)
                reader = [dict([key, int(value)] for key, value in d.items())
                          for d in reader]
                return [cls.create(**d) for d in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """static method that opens a window and draws
        all the Rectangles and Squares

        Args:
            list_rectangles (list) a list of rectangles to draw
            list_squares (list) a list a squares to draw

        """
        wn = turtle.Screen()
        wn.bgcolor("light green")
        wn.title("Task 21")
        skk = turtle.Turtle()

        for rec in list_rectangles:
            skk.penup()
            skk.goto(rec.x, rec.y)
            skk.pendown()
            for i in range(2):
                skk.forward(rec.width)
                skk.right(90)
                skk.forward(rec.height)
                skk.right(90)

        for sq in list_squares:
            skk.penup()
            skk.goto(sq.x, sq.y)
            skk.pendown()
            for i in range(4):
                skk.forward(sq.size)
                skk.right(90)
        
        turtle.exitonclick()
