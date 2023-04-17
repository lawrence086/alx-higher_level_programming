#!/usr/bin/python3
"""This module defines a base class for all other classes."""

import json


class Base:
    """The base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of the Base class.

        Args:
            id (int): The ID of the new instance, or None if not specified.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): The list of dictionaries to be converted.

        Returns:
            str: The JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write a JSON string representation of a list of objects to a file.

        Args:
            list_objs (list): The list of objects to be written to the file.

        Returns:
            None
        """
        file_name = cls.__name__ + ".json"
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(cls.to_dictionary(i))
        with open(file_name, 'w') as json_file:
            json_file.write(cls.to_json_string(new_list))

    def from_json_string(json_string):
        """Convert a JSON string representation into a list of dictionaries.

        Args:
            json_string (str): The JSON string to be converted.

        Returns:
            list: The list of dictionaries that was converted from the
            JSON string.
        """
        if json_string is None or json_string == 0:
            return []
        return json.loads(json_string)
