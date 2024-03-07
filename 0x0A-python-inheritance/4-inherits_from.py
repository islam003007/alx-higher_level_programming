#!/usr/bin/python3
"""this module has function that checks for inheritance"""


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class)
