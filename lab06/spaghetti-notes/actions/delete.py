"""
This module provides functions for deleting notes stored in a JSON file.

"""
from .json_handler import read_json, write_json


def delete(title: str) -> None:
    """
    Deletes the note with specified title from the JSON file.
    This function reads the existing notes from a JSON file, searches for a note with the specified
    title and then saves the other notes in the JSON file. If a note with the specified title is not
    found, it displays an appropriate message.
    :param title: The title of the note to be deleted.
    :return:
    """
    notes = read_json()

    if title not in notes:
        print("Doesn't exist, can't delete.")
    else:
        del notes[title]
        write_json(notes)
        print("Deleted.")
