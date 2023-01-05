#!/usr/bin/python3
"""
This is the 3-say_my_name module.
It contains 1 functions: say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    prints the string "My name is <first_name> <last_name>"
    checks if first_name is a string
    checks if last_name is a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
