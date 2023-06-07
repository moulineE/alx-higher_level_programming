#!/usr/bin/python3
flag = 0
y = 0
for i in range(122, 96, -1):
    print("{}".format(chr(i - y)), end="")
    if flag % 2 == 0:
        y = 32
    else:
        y = 0
    flag = flag + 1
