#!/usr/bin/python3
"""
A Function that returns the lists of available attributes and
methods of an object

"""


def lookup(obj):
    """
    Args:
    obj (object): object.

    """
    return (dir(obj))
