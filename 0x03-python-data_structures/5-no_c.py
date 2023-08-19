#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ""
    for char in my_string:
        if not ((char == 'c') or (char == 'C')):
            my_new_string += char
    return my_new_string
