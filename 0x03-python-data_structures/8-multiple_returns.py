#!/usr/bin/python3

def multiple_returns(string):
    if string == '':
        return (0, None)
    return (len(string), string[0])
