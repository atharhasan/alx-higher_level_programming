#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list
    idx = new_list.find(search)
    new_list.replace(idx, replace)
    return new_list
