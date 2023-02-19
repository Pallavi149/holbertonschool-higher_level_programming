#!/usr/bin/python3
"""
Module containing Base class
"""
import json
import os.path


class Base:
    """class Base with private class attribute __nb_objects"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation of an object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def get_nb_objects():
        return Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a JSON string representation of a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation json_string
        """
        if json_string is None:
            json_string = []
            return json_string

        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the given JSON string (given by to_json_string)
        of list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as f:
            dict_list = []
            for obj in list_objs:
                dict_list.append(obj.to_dictionary())
            j_string = cls.to_json_string(dict_list)
            f.write(j_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Using a dummy instance, returns an
        instance with pre-set attributes using kwargs
        """
        if cls.__name__ == "Square":
            dummy = cls(10)
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Public method that returns a list of instances
        """
        list_josn_obj = []
        list_obj = []
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                list_josn_obj = cls.from_json_string(f.read())
                for obj in list_josn_obj:
                    list_obj.append(cls.create(**obj))
        return list_obj
