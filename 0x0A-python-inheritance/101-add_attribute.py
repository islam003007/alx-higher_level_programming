#!/usr/bin/python3
"""this module has a function that adds attributes"""


def add_attribute(obj, att, attval):
    """adds atributes"""

    if not hasattr(prmObject, "__dict__"):
        raise TypeError("can't add new attribute")

    obj.att = attval
