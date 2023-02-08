#!/usr/bin/python3
"""
Module "6-base_geometry" including "BaseGeometry" class
and public instance method "area"
"""


class BaseGeometry:
    """
    A class with public instance method "area"
    """
    def area(self):
        """public instance method that raises an exception"""
        raise Exception("area() is not implemented")
