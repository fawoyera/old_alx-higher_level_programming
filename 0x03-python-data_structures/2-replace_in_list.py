#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        return None
    for i in my_list:
        if my_list.index(i) == idx:
            my_list[idx] = element
            return my_list
