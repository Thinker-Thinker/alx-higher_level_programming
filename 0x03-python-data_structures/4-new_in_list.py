#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in my_list:
        new_list.append(my_list[i - 1])
    if (idx >= 0) and (idx < len(new_list)):
        new_list[idx] = element
        return new_list
    else:
        return new_list
