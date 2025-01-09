"""
This module provides functions for reading and writing JSON data to and from files.
"""
import os
import json


def read_json(file_name: str = "notes.json") -> dict:
    """
    Opens json file and returns the notes in it.
    :param file_name: name of json file
    :return: Returns the notes saved into a dictionary.
    """
    notes = None
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            try:
                notes = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Error: Failed to decode JSON from {file_name}.\n{e}")
                notes = {}
            except IOError as e:
                print(f"Error: IOError occurred while reading {file_name}: {e}")
                notes = {}
    else:
        notes = {}
    return notes


def write_json(notes: dict, file_name: str = "notes.json") -> None:
    """
    Opens json file and writes notes in it.
    :param notes: a dictionary consisting of notes.
    :param file_name: the name of the json file
    """
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(json.dumps(notes))
