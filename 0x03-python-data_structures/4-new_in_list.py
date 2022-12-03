#!/usr/bin/python3
# new_in_list:replaces an element in a list at a specific position

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    new_list = copy = [x for x in my_list]
    new_list[idx] = element
    return (new_list)
