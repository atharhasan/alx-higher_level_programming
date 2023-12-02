#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_str = my_string.remove(my_string[i])
    return new_str
