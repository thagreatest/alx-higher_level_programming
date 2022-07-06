#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    for i in range(len(argv) - 1):
        sum += int(argv[i + 1])
    print("{}".format(sum))
