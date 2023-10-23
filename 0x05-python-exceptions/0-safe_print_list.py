#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listp = 0
    try:
        for i in range(0, x):
            listp = listp + 1
            print("{}".format(my_list[i]) end="")
        return listp
    except IndexError:
        return listp
