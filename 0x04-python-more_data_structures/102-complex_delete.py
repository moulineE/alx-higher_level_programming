#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = list(a_dictionary)
    for i in key_list:
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
