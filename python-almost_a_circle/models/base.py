#!/usr/bin/python3
"""
Module containing Base class
"""


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
