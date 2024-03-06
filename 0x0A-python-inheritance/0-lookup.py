#!/usr/bin/python3
"""provides a function that returnsa\
list of available attributes and methods"""


def lookup(obj):
    """ returns a list of available attributes and methods"""

    return dir(obj)
