#!/usr/bin/python3
# search_replac:
#  replaces all occurrences of an element by another in a new list
def search_replace(my_list, search, replace):
    my_list1 = my_list.copy()
    i = my_list1.index(search)
    my_list1.pop(i)
    my_list1.insert(i, replace)
    return (my_list1)
