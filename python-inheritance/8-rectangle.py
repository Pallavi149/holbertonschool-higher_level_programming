#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""
Class Rectangle inherits from BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """Instantiation of width and height """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
