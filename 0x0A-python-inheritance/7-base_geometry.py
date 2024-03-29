#!/usr/bin/python3
"""
A class that defines the attributes of Geometric Shapes
"""


class BaseGeometry:
    """
    a method that defines the area of a geometric shape
    """

    def area(self):
        raise Exception("area() is not implemented")

    """
    Arguments:
    name: name of the object
    value: value of the object
    """

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
