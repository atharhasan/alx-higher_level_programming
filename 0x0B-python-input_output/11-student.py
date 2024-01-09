#!/usr/bin/python3
'''Module containing class student'''


class Student:
    """class student

    Args:
    first_name: the student's first name
    last_name: the student's last name
    age: the student's age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for item in attrs:
            try:
                new_dict[item] = self.__dict__[item]
            except Exception:
                pass
        return new_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): json object.
        """
        self.__dict__.update(json)
