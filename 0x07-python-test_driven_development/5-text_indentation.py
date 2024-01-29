#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these characters: ., ? and :"""
    
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in (".", "?", ":"):
            print("\n")
            i+=1
        i+=1

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
