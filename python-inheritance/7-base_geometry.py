#!/usr/bin/python3
""" Class that defines BaseGeometry """


class BaseGeometry:
    def area(self):
        """public instance method that raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method Validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
