"""
Command-line Note-Taking Application

This script provides a command-line interface (CLI) for managing notes.
It supports the following actions:

- add: Adds a new note with a specified title, content, and optional due date.
- view: Displays the content of an existing note by title.
- delete: Deletes a note based on its title.
- list: Lists all available notes with their titles and due dates.
- edit: Edits the content and/or due date of an existing note.

Usage:
    python main.py <action> [--title <title>] [--content <content>] [--due-date <due_date>]

Where <action> is one of: add, view, delete, list, or edit.

The script uses the argparse library to parse command-line arguments and call the appropriate
action functions from the 'actions' module. If an invalid or incomplete input is provided,
error messages are displayed to guide the user through the necessary steps.
"""

from actions.add import add
from actions.view import view
from actions.delete import delete
from actions.list_notes import list_notes
from actions.edit import edit


try:
    import argparse
    parser = argparse.ArgumentParser(description="Command-line Note-Taking Application")
    parser.add_argument("action", choices=["add", "view", "delete", "list", "edit"],
                        help="What do you want to do?")
    parser.add_argument("--title", help="Title of the note")
    parser.add_argument("--content", help="Content of the note (only for `add` action)")
    parser.add_argument("--due-date", help="Optional due date (only for `add` action)")
    args = parser.parse_args()

    if (args.action in ("add", "view", "delete", "edit") and
            (args.title is None or args.title == "")):
        print("Need title.")

    if args.action == "add":
        if args.content is None:
            print("Needs content.")
        else:
            add(args.title, args.content, args.due_date)

    elif args.action == "view":
        view(args.title)
    elif args.action == "delete":
        delete(args.title)
    elif args.action == "list":
        list_notes()
    elif args.action == "edit":
        edit(args.title, args.content, args.due_date)
    else:
        print("Invalid action.")
except argparse.ArgumentError as e:
    print(f"Argument error: {e}")
except KeyError as e:
    print(f"Key error: {e}")
except ValueError as e:
    print(f"Value error: {e}")
