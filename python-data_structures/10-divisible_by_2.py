#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for item in range(len(new_list)):
        if new_list[item] % 2 == 0:
            new_list[item] = True
        else:
            new_list[item] = False
    return new_list
