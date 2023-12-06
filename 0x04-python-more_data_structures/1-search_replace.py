#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list
    idx = new_list.find(search)
    if idx != -1 :
        new_list.replace(idx, replace)
    return new_list
