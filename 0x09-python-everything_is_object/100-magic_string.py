#!/usr/bin/python3
def magic_string(dict={"num": 0}):
    dict["num"] += 1
    return ("BestSchool, " * dict["num"])[:-2]
