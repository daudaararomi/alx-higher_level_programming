#!/usr/bin/python3
# safe_print_integer - prints an integer with "{:d}".format()
# arg : value - can be any type (integer, string, etc.)
def safe_print_integer(value):
    try:
        if value is int:
            print("{:d}".format(value))
            return (True)
    except (TypeError, ValueError):
        return (False)
