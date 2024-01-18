#!/usr/bin/python3
'''Module containing class square that inherits from Rectangle'''

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ str special method"""
        str_rec = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}".format(self.size)

        return str_rec + str_id + str_xy + str_wh

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        if args is not None and len(args) is not 0:
            list_args = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_args[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        list_attr = ["id", "size", "x", "y"]
        dict_res = {}

        for key in list_attr:
            dict_res[key] = getattr(self, key)
        return dict_res
