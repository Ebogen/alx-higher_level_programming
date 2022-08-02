#!/usr/bin/python3
"""
Class that defines a rectangle from BaseGeometry Class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    We Initializes instance
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """
    The method returns the area of the instance
    """
    def area(self):

        return self.__width * self.__height
    """
    This is a special method that returns the printable string
    """
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
