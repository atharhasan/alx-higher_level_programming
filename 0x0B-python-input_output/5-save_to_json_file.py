#!/usr/bin/python3
'''Module containing the function save_to_json_file'''
import json


def save_to_json_file(my_obj, filename):
    """ function that writes an Object to a text file,
    using a JSON representation

    Args:
    my_obj: the obj that will write to a text file
    filename: the name of file that will writes on it.
    """

    with open(filename, "w") as file:
        json_obj = json.dump(my_obj)
        file.write(json_obj)
        file.close()
