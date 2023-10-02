#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """a function that find the biiger interger in a list"""
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
