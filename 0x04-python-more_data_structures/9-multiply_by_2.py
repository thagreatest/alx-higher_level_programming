#!/usr/bin/python3

def in_two_places(a_dictionary):
    return {k: a_dictionary[k] * 2 for (k, value) in a_dictionary.items()}
