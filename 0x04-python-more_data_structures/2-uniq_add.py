#!/usr/bin/python3
# adds all unique integers in a list (only once for each integer)

def uniq_add(my_list=[]):
    sum = 0
    for x in set(my_list):
        sum += x
    return (sum)
