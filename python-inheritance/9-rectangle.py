#!/usr/bin/python3
""" Class Rectangle inherits from BaseGeometry class """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle is a subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """ Instantiation of width and height """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of a rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        Informal string representation of a rectangle
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
