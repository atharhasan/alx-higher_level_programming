#!/usr/bin/python3
"""Define a class named Square."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
        size: Private instance attribute for square.
        """
        self.size = size

    @property
    def size(self):
        """That retrive the size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """to sit the size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method that returns the current square area"""
        return self.__size * self.__size
