#!/usr/bin/python3
'''9-Rectangle.py'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherite from BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns area of Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        '''String representation method.'''
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
