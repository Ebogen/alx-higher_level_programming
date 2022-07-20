#!/usr/bin/python3


""" A class Square """


class Square:
    """ Here we initialize the square object """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:

            self.__size = int(size)