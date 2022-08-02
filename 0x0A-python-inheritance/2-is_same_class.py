#!/usr/bin/python3

"""
Functions that returns True if the object is exactly an
instance of the specific class: otherwise False.

"""


def is_same_class(obj, a_class):

    """
    Args:
    obj: object
    a_class: class type

    Returns:
        True if type of obj is a_class
        False, otherwise

    """
    return type(obj) is a_class
