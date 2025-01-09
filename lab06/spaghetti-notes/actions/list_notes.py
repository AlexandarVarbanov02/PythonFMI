"""
This module provides functions for listing notes stored in a JSON file.
"""
from .json_handler import read_json


def list_notes() -> None:
    """
    Lists all the notes stored in a JSON file.

    This function reads the notes from a JSON file and prints the title and due date of each note.
    If there are no notes, a message is displayed indicating that there is nothing to list.
    """
    notes = read_json()

    print("Listing notes...")
    if len(notes) == 0:
        print("Nothing to list.")
    else:
        for title in notes:
            print("- " + title + " (Due: " + (notes[title]["due_date"] if notes[title]["due_date"]
                                              else "None") + ")")
