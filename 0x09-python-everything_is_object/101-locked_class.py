#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if not hasattr(self, 'first_name') and name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        self.__dict__[name] = value
