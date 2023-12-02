#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(0, len(my_list)):
        new_list = my_list[i].reverse()
        print("{:d}".format(new_list))
    return new_list
