#!/usr/bin/python3
'''Module containing class Rectangle that inherits from Base'''

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """the method that returns the area value"""
        return (self.width * self.height)

    def display(self):
        """ that prints in stdout the Rectangle instance
        with the character #"""
        rec = self.y * "\n"
        for i in range(self.height):
            rec += " " * self.x + "#" * self.width + "\n"
        print(rec, end='')

    def __str__(self):
        """ str special method"""
        str_rec = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return str_rec + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if args is not None and len(args) is not 0:
            list_args = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
