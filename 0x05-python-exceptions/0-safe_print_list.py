#!/usr/bin/python3
#safe_print_list - prints x elements of a list

def safe_print_list(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{}".format(my_list[i]), end='')
            i = i + 1
        except IndeError:
            break
    print()
    return i
