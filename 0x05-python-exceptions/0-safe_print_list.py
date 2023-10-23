#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    listp = ""
    try:
        for i in range(0, x + 1):
            listp = listp + str(my_list[i])
        return int(listp)
    except IndexError:
        return int(listp)
