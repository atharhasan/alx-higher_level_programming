#!/usr/bin/python3

def read_file(filename=""):
    """function that read file"""

    with open(filename, "r", encoding="UTF8") as file:
        print(file.read(), end="")
