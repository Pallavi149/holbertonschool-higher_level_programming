#!/usr/bin/python3
"""
A class named Student
"""


class Student:
    """
    A class that defines students
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation of students
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return: dict representation of Student instances
        """
        attr_dict = {}
        if type(attrs) == list:
            for att in attrs:
                if hasattr(self, att):
                    attr_dict[att] = getattr(self, att)
            return attr_dict
        return(self.__dict__)
