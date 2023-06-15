#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    keylist = list(a_dictionary)
    for i in keylist:
        new_dictionary[i] = new_dictionary[i] * 2
    return new_dictionary
