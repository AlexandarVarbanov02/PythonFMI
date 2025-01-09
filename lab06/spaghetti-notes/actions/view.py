"""
This module provides functions for searching and viewing notes stored in a JSON file.
"""
from .json_handler import read_json


def view(title: str) -> None:
    """
    Prints the content and due date of the note with given title.

    This function reads the notes from a JSON file and displays the content and due date
    of the note with the specified title. If the title is empty or a note with that title
    does not exist, appropriate message is displayed.
    :param title: The title of the note to be viewed.
    :return:
    """
    notes = None
    notes = read_json()

    if title not in notes:
        print("Doesn't exist.")
    else:
        print(title)
        print("---")
        print(notes[title]["content"])
        print("---")
        if notes[title]["due_date"]:
            print("Due:" + notes[title]["due_date"])
        else:
            print("No due date.")
