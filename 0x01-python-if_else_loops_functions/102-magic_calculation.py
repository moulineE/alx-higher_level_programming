#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    if c > b:
        return a + b
    b = a * b
    c = b - c
    return (c)
