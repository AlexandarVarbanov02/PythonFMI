"""
This module provides functions for editing notes kept in a JSON file.
    
It allows the user to find a note by its title, and then edit the content and/or 
due date of the note. The notes are read from and written to a JSON file.

"""
from .json_handler import read_json, write_json


def edit(title, content, due_date) -> None:
    """
    Finds the node with the same title and edits its contents and prints an appropriate message.
    :param title: Name/title of the note to edit
    :param content: The new content to be edited in the note
    :param due_date: The new due date to be edited in the not
    """
    notes = None
    notes = read_json()

    if title not in notes:
        print(f"Note with title {title} does not exist.")
    elif content is None and due_date is None:
        print("No content or due date provided - no changes made to the note.")
    else:
        note = notes[title]
        if content is not None:
            note["content"] = content
        if due_date == "none":
            note["due_date"] = None
        elif due_date is not None:
            note["due_date"] = due_date

        write_json(notes)

        print("Note successfully edited.")
