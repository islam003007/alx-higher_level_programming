#!/usr/bin/python3
"""defines a class square"""


class Square:
    """a square class"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, a):
        if type(a) is not tuple and len(a) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(a[0]) is not int and type(a[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")

        if a[0] < 0 or a[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")

        self.__position = a
