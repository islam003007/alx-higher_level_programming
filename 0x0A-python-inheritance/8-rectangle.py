#!/usr/bin/python3
"""this module has a rectangle class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class rectangle(BaseGeometry):
    """a rectangle class that inherits from BaseGeonmetry"""

    def __init__(self, width, height):
        """initlizes instance of triangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
