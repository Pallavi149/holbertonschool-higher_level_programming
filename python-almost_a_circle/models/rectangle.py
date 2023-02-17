#!/usr/bin/python3
"""
Module containing class Rectangle inherits from base class Base
"""
from models.base import Base


class Rectangle(Base):
    """Class that defines a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for instantiation of a Rectangle.
        Super class called with id
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width """
        return self.__width

    @property
    def height(self):
        """Getter for height """
        return self.__height

    @property
    def x(self):
        """Getter for x """
        return self.__x

    @property
    def y(self):
        """Getter for y """
        return self.__y

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter for x """
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method that return the area of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """public method that prints in stdout the
        Rectangle instance with the character # """
        for i in range(self.__y):
            print()
        for item in range(self.__height):
            print(' ' * self.__x, end="")
            print('#' * self.__width)

    def __str__(self):
        """Returns a string representation of a rectangle"""
        return (f"[Rectangle] ({self.id}) {self.__x}\
        /{self.__y} - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """ public method that assigns an argument to each attribute
        If args is given in key, value pairs, arg goes through **kwargs
        """
        for key, value in kwargs.items():
            if key == "width":
                self.width = value
            elif key == "height":
                self.height = value
            elif key == "x":
                self.x = value
            elif key == "y":
                self.y = value
            elif key == "id":
                self.id = value
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        """Dictionary representation of a Rectangle"""
        s_dict = {}
        s_dict["id"] = self.id
        s_dict["size"] = self.width
        s_dict["size"] = self.height
        s_dict["x"] = self.x
        s_dict["y"] = self.y
        return s_dict
