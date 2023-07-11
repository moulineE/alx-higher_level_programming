#!/usr/bin/python3
"""This module define a function that write a text file and
return the number of character"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str): the filename of the text file to write in
        text (str): the strig to add to the file 'filename'
    Returns:
        the number of character added

    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
