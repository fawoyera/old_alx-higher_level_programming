#!/usr/bin/python3
"""Script that adds all arguments to a python list and save them to a file"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        python_list = load_from_json_file(filename)
    except FileNotFoundError:
        python_list = []
    python_list.extend(sys.argv[1:])
    save_to_json_file(python_list, filename)
