#!/usr/bin/python3
"""
This is "0-add_integer" module, it supllies one function, add_integer().
"""

def add_integer(a, b=98):
    """
    Adds two numbers and returns the result. Second argument to this
    function is optional and it has default value of 98.
    """
    if  a is None or not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    result = a + b
    if result == float('inf') or result == -float('inf'):
        raise ValueError("cannot convert float NaN to integer")
    return  int(a) + int(b)
