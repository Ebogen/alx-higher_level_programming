#!/usr/bin/python3
"""
a function that writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Arguments:
    my_obj (object): object to be serialized.
    filename (str): name of file where string is stored.
    """
    with open(filename, "w") as j_file:
        json.dump(my_obj, j_file)
