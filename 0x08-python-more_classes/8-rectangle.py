#!/usr/bin/python3
"""Define a class named Rectangle."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
    number_of_instances: represent the number of rectangle instance.
    print_symbol: that can print symbol
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intial new rectangle.

        Args:
        width (int): the width of rectangle.
        height (int): the height of rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of rectangle that equal width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """That print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        myList = []
        for i in range(self.__height):
            [myList.append(str(self.print_symbol))for j in range(self.__width)]
            if i != self.__height - 1:
                myList.append("\n")
        return "".join(myList)

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print the message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ returns the biggest rectangle based on the area.

        Args:
        rect_1 (Rectangle): the first rectangle.
        rect_2 (Rectangle): the second rectangle.
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
