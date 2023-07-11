#!/usr/bin/python3
"""This module define a lopkup function that look for atribut and
methods of an object"""

def lookup(obj):
    """returns the list of available attributes and methods of an
    object"""
    return (dir(obj))
