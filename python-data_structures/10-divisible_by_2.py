#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    new_list = list(my_list)
    for item in range(len(new_list)):
        if item % 2 == 0:
            new_list[item] = True
        else:
            new_list[item] = False
    return new_list
