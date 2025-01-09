"""
This module contains functions for managing and manipulating notes stored in a JSON file.

The actions provided in this module include:
- Adding new notes with a title, content, and optional due date.
- Viewing the content and due date of a specific note by its title.
- Editing the content or due date of an existing note.
- Deleting notes by title.
- Listing all available notes along with their due dates.

These functions interact with the notes stored in a JSON file, using the read_json and write_json
functions from the json_handler module to load and save note data.

Functions:
    add(title, content, due_date): Adds a new note with the specified title, content, and
    optional due date.
    view(title): Displays the content and due date of the note with the given title.
    edit(title, content, due_date): Edits the content and/or due date of an existing note.
    delete(title): Deletes the note with the given title.
    list_notes(): Lists all the notes, displaying their titles and due dates.

"""

from .json_handler import read_json, write_json
