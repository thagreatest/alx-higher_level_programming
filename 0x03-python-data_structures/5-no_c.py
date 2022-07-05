#!/usr/bin/python3

def no_c(my_list):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == 'c' or new_list[i] == 'C':
            new_list[i] = 0
    return new_list
