#!/usr/bin/python3
"""
A function that returns True if the object is an instance
of, or if the object is an instance of a class inherited from,
the Aspecified class; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    Arguments:
    obj: object
    a_class: class type

    Return: the value true if obj is an instance of a_class
    else False.
    """

    return isinstance(obj, a_class)
