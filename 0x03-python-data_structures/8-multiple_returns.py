#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        char = None
    else:
        char = sentence[0]
    return sen_len, char
