#!/usr/bin/python3
"""This module define a sub class that inherit a list and print it
sorted"""


class MyList(list):
    """subclass that sorte a list and print it"""

    def print_sorted(self):
        """Public instance method that prints the list, but sorted"""
        return (sorted(self))
