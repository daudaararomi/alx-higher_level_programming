#!/usr/bin/python3
""" contains the number_of_lines function """


def number_of_lines(filename=""):
    """ returns the number of lines in a file """
    i = 0
    with open(filename) as f:
        for line in f:
            i += 1
    return i
