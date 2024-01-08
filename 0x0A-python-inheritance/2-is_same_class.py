#!/usr/bin/python3
'''2-is_same_class.py'''


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class

    Args:
    obj: the first arg that we want to check
    a_class: the second arg that we want to compare with
    """
    return type(obj) == a_class
