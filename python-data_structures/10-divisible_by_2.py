#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for item in new_list:
        if item % 2 == 0:
            new_list[item] = True
        else:
            new_list[item] = False
    return new_list
