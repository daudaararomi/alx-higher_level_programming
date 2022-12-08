#!/usr/bin/python3
# update_dictionary:
# replaces or adds key/value in a dictionary
def update_dictionary(a_dictionary, key, value):
    for k in a_dictionary:
        if k == key:
            del a_dictionary[k]
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
    return (a_dictionary)
