#!/usr/bin/python3
""" Here we define a square by its size"""


class Square:
    """ initialize the square object"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ return the square area of the object """
        return (self.__size ** 2)

    @property
    def size(self):
        """ return the size value"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size value of the square object """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
