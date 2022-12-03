#!/usr/bin/python3
# no_c : removes all characters c and C from a string

def no_c(my_string):

    new_string = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(new_string))
