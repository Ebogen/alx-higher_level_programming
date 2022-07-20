#!/usr/bin/python3


""" A class that defines a square by its size """


class Square:
    """ Here we initialize the class object """

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ We return the square area of the object """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Here we return the size value """

        return self.__size

    @size.setter
    def size(self, value):
        """ Here we set the size value of the square object """

        if not is isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
