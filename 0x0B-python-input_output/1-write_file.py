#!/usr/bin/python3
""" contains the number_of_lines function """


def number_of_lines(filename=""):
    """ returns the number of lines in a file """
    cnt = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            count += 1
    return count
