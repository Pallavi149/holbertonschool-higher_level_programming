#!/usr/bin/python3
"""
Module containing "Square" subclass that inherits
from "Rectangle" subclass of "Base" class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class that represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Instantiation of a rectangle """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Returns a string representation of a square"""
        return(f"[Square] ({self.id}) {self.x}/\
{self.y} - {self.height}")

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        for key, value in kwargs.items():
            if key == 'size':
                self.size = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value
            if key == 'id':
                self.id = value

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """Dictionary representation of a Square"""
        s_dict = {}
        s_dict["id"] = self.id
        s_dict["x"] = self.x
        s_dict["size"] = self.size
        s_dict["y"] = self.y
        return s_dict
