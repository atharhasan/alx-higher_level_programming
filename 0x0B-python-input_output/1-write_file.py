#!/usr/bin/python3
'''1-write_file'''


def write_file(filename="", text=""):
    """function that writes a string to a text file"""

    with open(filename, "w", encoding="UTF8") as file:
        return file.write(text)
