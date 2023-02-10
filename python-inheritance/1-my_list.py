#!/usr/bin/python3
"""Class that defines MyList """


class MyList(list):
    """Class MyList inherited from class list"""
    def print_sorted(self):
        print(sorted(self))
