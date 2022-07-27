#!/usr/bin/python3
"""
A module that contains a class that avoids
dynmaically created attributes
"""


class LockedClass:
    __slots__ = ['first_name']
