#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} * {} = {}".format(a, b, (mul(a, b))))
    elif op == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
