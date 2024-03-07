#!/usr/bin/python3
"""this module has function that cis like isinstance()"""


def is_same_class(obj, a_class):
    """isinstance() clone"""
    if type(obj) == a_class:
        return True
    else:
        return False
