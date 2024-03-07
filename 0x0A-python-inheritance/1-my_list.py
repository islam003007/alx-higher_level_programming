#!/usr/bin/python3
"""this module has MyList class"""


class MyList(list):
    """custom class of list"""

    def print_sorted(self):
        """prints a list sorted"""
        temp = self[:]
        temp.sort()
        print(temp)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
