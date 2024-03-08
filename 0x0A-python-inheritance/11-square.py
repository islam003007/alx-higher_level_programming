#!/usr/bin/python3
"""this module has an improved square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """an improved Square class that inherits from Rectangle"""

    def __init__(self, size):
        """initializes a square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
