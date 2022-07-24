#!/usr/bin/python3
"""

A function that adds two numbers


"""


def add_integer(a, b=98):
    """ Adds two integer or float numbers

    Args are:
    a: first number
    b: second number

    Return:
    The addition of two numbers


    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer ")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer ")

    """We now convert a and b to integers"""
    a = int(a)
    b = int(b)
    return (a + b)
