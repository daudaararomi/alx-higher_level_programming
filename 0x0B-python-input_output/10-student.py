#!/usr/bin/python3
""" contains the class Student """


class Student:
    """ defines class Student """

    def __init__(self, first_name, last_name, age):
        """ initalizes new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

def to_json(self, attrs=None):
    """Retrieves dictionary of Student with conditions to filter
    """

    if attrs == None or type(attrs) != list:
        return self.__dict__
    else:
        temp = {}
        for elem in attrs:
            if type(elem) != str:
                return self.__dict__
            if elem in self.__dict__.keys():
                temp[elem] = self.__dict__[elem]
    return temp