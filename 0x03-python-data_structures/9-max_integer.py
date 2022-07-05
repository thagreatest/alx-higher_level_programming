#!/usr/bin/python3

def max_integer(list = []):
    if list == []:
        return None
    else:
        max = list[0]
        for i in list:
            if i > max:
                max = i
        return max
