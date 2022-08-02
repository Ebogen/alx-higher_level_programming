#!/usr/bin/python3

"""
A class that defines a rectangle from BaseGeometry Class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    we initialize instance
    """

    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
