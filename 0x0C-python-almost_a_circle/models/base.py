#!/usr/bin/python3
""" this module contains the class Base """


class Base:
    """ empty Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes Base """
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
