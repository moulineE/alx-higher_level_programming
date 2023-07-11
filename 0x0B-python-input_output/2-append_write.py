#!/usr/bin/python3
"""This module define a function that appends a string at the end of a
text file and return the number of character added"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added

    Args:
        filename (str): the filename of the text file to write in
        text (str): the strig to add to the file 'filename'
    Returns:
        the number of character added

    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
