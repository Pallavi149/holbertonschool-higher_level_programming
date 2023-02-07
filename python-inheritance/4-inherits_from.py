#!/usr/bin/python3
"""
Module containing the inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Returns True or False depending upon whether an object
    is an instance of a subclass of a_class
    """
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
