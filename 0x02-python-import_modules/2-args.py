#!/usr/bin/python3
from sys import argv as args

if __name__ ==  '__main__':

    count = len(args) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in count:
        print("{}: {}".format(i + 1, args[i + 1]))

