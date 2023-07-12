#!/usr/bin/python3
"""This module define a function that returns the dictionary description
with simple data structure for JSON serialization of an object"""


def class_to_json(obj):
    """a function that returns the dictionary description from JSON"""
    return obj.__dict__
