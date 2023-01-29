#!/usr/bin/python3
def roman_to_int(roman_string):
    # Fail checks, none, not a string
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    # Dictionary for roman numerals
    r_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    length = len(roman_string)
    for i in range(length):
        value = r_dict.get(roman_string[i])
        if i < (length - 1) and value < r_dict.get(roman_string[i + 1]):
            result = result - value
        else:
            result = result + value
    return result
