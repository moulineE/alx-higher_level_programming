#!/usr/bin/python3
def no_c(my_string):
    i = 0
    new_string = my_string[::-1][::-1]
    while len(new_string) - 1 > i:
        if new_string[i] == "C" or new_string[i] == "c":
            new_string = new_string[:i] + new_string[i+1:]
            continue
        else:
            i += 1
    return new_string
