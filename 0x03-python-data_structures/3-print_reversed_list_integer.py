#!/usr/bin/python3
# 3-print_reversed_list_integer.py
# Print all integers of a\eads list in reverse order.


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
