#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, sub, div
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    m = int(sys.argv[1])
    n = int(sys.argv[3])
    if sys.argv[2] == "+":
        print("{} + {} = {}".format(m, n, add(m, n)))
    elif sys.argv[2] == "-":
        print("{} - {} = {}".format(m, n, sub(m, n)))
    elif sys.argv[2] == "*":
        print("{} * {} = {}".format(m, n, mul(m, n)))
    elif sys.argv[2] == "/":
        print("{} / {} = {}".format(m, n, div(m, n)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
