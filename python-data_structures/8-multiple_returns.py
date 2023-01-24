#!/usr/bin/python3
def multiple_returns(sentence):
    my_string = sentence
    length = len(my_string)
    if my_string is None:
        return None
    else:
        return (length, my_string[0])
