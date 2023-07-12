#!/usr/bin/python3
import json
"""This module define a function that returns the JSON representation
of an object (string)"""


def to_json_string(my_obj):
    """a function that returns the JSON representation of an
    object (string):"""
    return json.dumps(my_obj)
