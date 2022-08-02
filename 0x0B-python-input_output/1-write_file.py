#!/urs/bin/python3
"""
 function that writes a string to a text file (UTF8) and returns the number
 of characters written
"""


def write_file(filename="", text=""):
    """
    Argument:
    filename: (str):f the file.
    text (str): text to be written
    """
    with open(filename, "w", encoding='utf-8') as a_file:
        return a_file.write(text)
