#!/usr/bin/python3i
def max_integer(my_list=[]):
    big = 0
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list) - 1):
            if my_list[i] > big:
                big = my_list[i]
    return big
