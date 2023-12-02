#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string
    for i in range(0, len(new_str)):
        if new_str[i] == 'c' or new_str[i] == 'C':
            new_str.remove(new_str[i])
    return new_str
