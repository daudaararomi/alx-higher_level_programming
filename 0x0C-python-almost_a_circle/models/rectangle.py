#!/usr/bin/python3
""" this module contains the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ empty class Rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes empty Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
