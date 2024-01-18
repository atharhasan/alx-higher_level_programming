#!/usr/bin/python3
'''Module containing class Base'''
import json
import csv
import os.path


class Base:
    """class Base

    Args:
    id (int) : an interger arg
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ that writes the JSON string representation
        of list_objs to a file"""
        filename = "{}.json".format(cls.__name__)
        list_dict = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dict)

        with open(filename, "w") as file:
            file.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ that returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(5, 5)
        else:
            new = cls(5)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins


    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Method that saves a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """ Method that loads a CSV file """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins
