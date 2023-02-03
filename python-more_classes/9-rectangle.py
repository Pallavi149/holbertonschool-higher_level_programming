#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """A class for a rectangle of given width and height
    Public class Attribute:
    number_of_instances
    print_symbol

    Private Attributes:
    __width (int): the width of the rectangle
    __height (int): the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialises the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greatest area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        else:
            return(rect_2)

    @property
    def width(self):
        """Property getter for __width. Returns the width"""
        return(self.__width)

    @width.setter
    def width(self, value):
        """Property setter for __width"""
        if not isinstance(value, int):
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
        return self.height * self.width

    def perimeter(self):
        """Public instance method returning the perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            pm = 2 * (self.width + self.height)
            return pm

    def __repr__(self):
        """Returns a reproducible string representation of a rectangle"""
        return(f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1

    def __str__(self):
        """Returns a printable string representation of a rectangle"""
        if self.__width != 0 and self.__height != 0:
            string = ""
            for i in range(1, self.__height):
                string = string + str(self.print_symbol) * self.__width + '\n'
            else:
                string = string + str(self.print_symbol) * self.__width
            return string
        return f""
