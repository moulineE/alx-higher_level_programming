#!/usr/bin/python3
def remove_char_at(str, n):
    """creates a copy of the string,
    removing the character at the position n"""
    if n < 0:
        return str
    strcopy = str[:n] + str[n + 1:]
    return strcopy
