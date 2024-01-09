#!/usr/bin/python3
'''Module containing the function append_write'''


def append_write(filename="", text=""):
    """function that append a string to a text file"""

    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
