#!/usr/bin/python3
"""this module has a square class"""


Rectangle = __import__("9-base_geometry").Rectangle


class Square(Rectangle):
    """a Square class that inherits from Rectangle"""

    def __init__(self, size):
        """initializes a square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2
