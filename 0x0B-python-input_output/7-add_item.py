#!/usr/bin/python3
"""
Adds all arguments to a Python list and saves them to a file.
"""


import sys
from typing import List
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(args: List[str], filename: str) -> None:
    """
    Adds all arguments to a Python list and saves them to a file.

    Args:
        args (List[str]): The arguments to add to the list.
        filename (str): The name of the file to save the list to.
    """
    try:
        my_list = load_from_json_file(filename)
    except FileNotFoundError:
        my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(sys.argv[1:], "add_item.json")
