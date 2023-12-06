#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list
    idx = new_list.index(search)
    if idx != -1 :
        new_list[idx] = replace
        return new_list
