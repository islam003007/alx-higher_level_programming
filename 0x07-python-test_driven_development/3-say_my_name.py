#!/usr/bin/python3
"""prints my name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """prints my name is <first name> <last name>"""
    
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    
    print("my name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
