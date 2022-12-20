#!/usr/bin/python3
# safe_print_list_integers -  prints the first x elements of a list and only integers.
# arg:
#     my_list: can contain any type (integer, string, etc.)
#     x:  represents the number of elements to access in my_list


def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end='')
            i = i + 1
        except(ValueError,TypeError):
            continue
        print(''
        return (i)
