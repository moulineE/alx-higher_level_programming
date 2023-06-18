#!/usr/bin/python3
def roman_to_int(roman_string):
    sym = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    res = 0
    if (not (isinstance(roman_string, str)) or roman_string is None):
        return 0
    pres = 0
    for i in roman_string:
        if i not in sym:
            return 0
        if pres >= sym[i]:
            res += sym[i]
        elif (pres < sym[i] and ((pres == 1 and (sym[i] == 5 or 10)) or
                                 (pres == 10 and (sym[i] == 50 or 100)) or
                                 (pres == 100 and (sym[i] == 500 or 1000)))):
            res += sym[i] - pres - pres
        else:
            res += sym[i]
        pres = sym[i]
    return res
