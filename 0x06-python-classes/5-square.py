#!/usr/bin/python3
"""defines a class square"""


class Square:
    """a square class"""

    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size ** 2
    
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, a):
        if type(a) is not int:
            raise TypeError("size must be an integer")

        if a < 0:
            raise ValueError("size must be >= 0")

        self.__size = a
