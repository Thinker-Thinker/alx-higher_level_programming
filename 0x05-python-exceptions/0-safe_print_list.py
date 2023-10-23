#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listp = 0
    try:
        for i in range(x):
            listp = listp + 1
            print("{:d}".format(my_list[i]), end="")
        print("")
        return listp
    except IndexError:
        print("")
        return listp
