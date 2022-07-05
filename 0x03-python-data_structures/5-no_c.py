#!/usr/bin/python3

def no_c(my_list):
    new_list = []
    for i in my_list:
        if i != 'c' and i != 'C':
            new = new_list.append(i)
        return new
