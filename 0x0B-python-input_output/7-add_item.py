#!/usr/bin/python3
"""Saving json objects to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Creating a file with json objects"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f, ensure_ascii=False)
