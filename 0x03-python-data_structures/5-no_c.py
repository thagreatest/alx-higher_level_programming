#!/usr/bin/python3

def no_c(my_list):
    new_list = my_list.translate({ord('c'): None , ord('C'): None})
    return new_list
