"""
This module provides functions for adding new notes to a JSON file.
"""
from .json_handler import read_json, write_json


def add(title: str, content: str, due_date: str) -> None:
    """
    Adds a new note with the specified title, content and optional due date. This function reads
    the existing notes from a JSON file and adds a new note if a note with the same title does
    not exist. If the title or content is empty, an error message is displayed.The due date is
    optional, and if not provided, it is set to None.
    :param title: Title of the note to be added.
    :param content: The content of the node.
    :param due_date: The due date for the note which is optional.
    :return:
    """
    notes = None
    notes = read_json()

    if content == "":
        print("No content, can't add note.")
    else:
        if title in notes:
            print("Already exists, won't overwrite.")
        else:
            if due_date:
                notes[title] = {
                    "content": content,
                    "due_date": due_date
                }
            else:
                notes[title] = {
                    "content": content,
                    "due_date": None
                }
            write_json(notes)
