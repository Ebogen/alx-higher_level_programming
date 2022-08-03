#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    Args:
    filename (str): name of file.
    """
    with open(filename, "r") as j_file:
        my_obj = json.load(j_file)
        return my_obj
