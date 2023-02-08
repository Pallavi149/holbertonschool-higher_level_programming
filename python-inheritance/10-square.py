#!/usr/bin/python3
"""Class Square that inheris from class Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square is a subclass of Rectangle
    which is a subclass of BaseGeometry
    """
    def __init__(self, size):
        """instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
