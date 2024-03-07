#!/usr/bin/python3
"""this module has function that checks for inheritance"""


def inherits_from(obj, a_class):
    """checks for inheritance"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class


a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
