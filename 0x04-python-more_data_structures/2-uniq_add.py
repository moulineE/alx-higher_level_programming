#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_addlist = set(my_list)
    add = 0
    for i in uniq_addlist:
        add = add + i
    return add
