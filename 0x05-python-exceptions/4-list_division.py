#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(list_length):
        try:
            list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            list.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            list.append(0)
        except IndexError:
            print("out of range")
            list.append(0)
        finally:
            pass
    return list
