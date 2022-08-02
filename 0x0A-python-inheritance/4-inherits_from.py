#!/usr/bin/python3
"""
A function that returns true or false if the object is an
instance of a_class
"""


def inherits_from(obj, a_class):
    """
    Arguments:
    obj: object
    a_class: class type

    Returns:
    the value of true if the object is an instance of a_class
    otherwise, false
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
