#!/usr/bin/python3
# max_integer
#  finds the biggest integer of a list.


def max_integer(my_list=[]):
    max = 0
    if len(my_list) == 0:
        return (None)

    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]

    return (max)
