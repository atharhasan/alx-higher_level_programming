#!/usr/bin/python3
'''10-square.py'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherite from Rectangle"""

    def __init__(self, size):
        if self.integer_validator('size', size):
            super().__init__(size, size)
            self.__size = size

    def area(self):
        """ Returns area of Square object"""
        return super().area()
