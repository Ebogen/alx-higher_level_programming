#!/usr/bin/python3
"""

A function that prints 2 new lines after ".?:" characters


"""


def text_indentation(text):
    """ prints 2 new lines after ".?:" characters


    Args:
    text: represents the input string

    """

    if type(text) is not str:
        raise TypeError("text msut be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s is "" else s + "\n\n" + i + d

    print(s[:-3], end="")
