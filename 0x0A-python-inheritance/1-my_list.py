#!/usr/bin/python3
'''1-my_list.py'''


class MyList(list):
    """class mylist that inherits from list"""
    def print_sorted(self):
        """ prints the sorted list """
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
