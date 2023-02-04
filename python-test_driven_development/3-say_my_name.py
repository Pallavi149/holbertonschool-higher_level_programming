#!/usr/bin/python3
"""
This is "3-say_my_name" module, it supllies one function, say_my_name().
"""


def say_my_name(first_name, last_name=""):
    """
    Function has two string arguments which represents first name and last name
    second argument 'last_name' is an optional
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
