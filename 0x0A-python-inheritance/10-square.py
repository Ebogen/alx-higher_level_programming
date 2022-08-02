#!/usr/bin/python3

"""
Represents a class that defines a Square from Rectangle class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """
    A method that initializes a Square
    """
    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    """
    the method that returns a string with the area
    """
    def area(self):

        return super().area()
