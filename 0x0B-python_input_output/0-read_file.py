#!/usr/bin/python3
"""file reader"""

def read_file(filename=""):
    """Reads a file"""
    
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
