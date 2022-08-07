#!/usr/bin/python3
"""
A module containing class Base
"""

import json
import csv
import os.path


class Base:
    """class base for the entire project. """
    __nb_objects = 0

    def __init__(self, id = None):
        """ Next we initialize the class attributes """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
