#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A class for a rectangle of given width and height
    Attributes:
    __width (int): the width of the rectangle
    __height (int): the height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """Initialises the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Property getter for __width. Returns the width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Property setter for __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property getter for __height. Returns the height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        """Property setter for __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method returning the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Public instance method returning the perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            pm = 2 * (self.__width + self.__height)
            return pm

    def __repr__(self):
        """Returns a reproducible string representation of a rectangle"""
        return(f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")

    def __str__(self):
        """Returns a printable string representation of a rectangle"""
        if self.__width != 0 and self.__height != 0:
            string = ""
            for i in range(1, self.__height):
                string = string + "#" * self.__width + '\n'
            else:
                string = string + "#" * self.__width
            return string
        return f""
