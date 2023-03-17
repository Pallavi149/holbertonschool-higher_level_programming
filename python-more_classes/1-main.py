#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
my_rectangle.foobar = 5
my_rectangle.__foobar = 42
my_rectangle.__width = 57
print("Before")
print(my_rectangle.__dict__)
my_rectangle._Rectangle__width = 13
print(my_rectangle.__dict__)
