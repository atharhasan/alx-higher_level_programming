#!/usr/bin/python3
'''Module containing class Base'''


class Base:
    """class Base

    Args:
    id (int) : an interger arg
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
