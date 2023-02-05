#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise data"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set position"""
        message_error = "position must be a tuple of 2 positive integers"
        if (type(value) != tuple or len(value) != 2):
            raise TypeError(message_error)

        for items in value:
            if type(items) != int or items < 0:
                raise TypeError(message_error)
        self.__position = value

    def area(self):
        """get area of square"""
        return self.__size ** 2

    def my_print(self):
        """print square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
