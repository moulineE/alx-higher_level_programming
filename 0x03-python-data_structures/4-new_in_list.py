#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        list_copy = my_list.copy()
        if (len(my_list) - 1 <= idx) or idx < 0:
            return list_copy
        else:
            list_copy[idx] = element
            return list_copy
