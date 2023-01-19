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

    @property
    def width(self):
        """ finds width """
        return self.__width

    @width.setter
    def width(self, value):
        """ validates width as a positive integer """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """ finds height """
        return self.__height

    @height.setter
    def height(self, value):
        """ validates height as a positive integer """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """ finds x """
        return self.__x

    @x.setter
    def x(self, value):
        """ validates x as a positive or zero integer """
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value
