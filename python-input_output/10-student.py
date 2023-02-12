#!/usr/bin/python3
"""
Module containing "Student" class
"""


class Student:
    """
    Representation of a student
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of a student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public instance method returning a JSON
        dictionary of a student instance. If attrs is
        a list of strings, a new dictionary is returned
        comprising only the attributes from attrs
        """
         attr_dict = {}
         if type(attrs) == list:
            for att in attrs:
                if hasattr(self, att):
                    attr_dict[att] = getattr(self, att)
            return attr_dict
        return(self.__dict__)
