import pytest
from unittest.mock import patch
from actions.list_notes import list_notes


# A pytest fixture to reset the in-memory storage
@pytest.fixture(autouse=True)
def reset_mock_storage():
    global mock_notes_storage
    mock_notes_storage = {"Title": {"content": "Content", "due_date": "2025-01-09"}}
    # Reset the storage before each test


# An in-memory dictionary to simulate the JSON storage
mock_notes_storage = {}


def mock_read_json():
    """Simulates reading from a JSON file."""
    return mock_notes_storage


@patch("actions.list_notes.read_json", side_effect=mock_read_json)
def test_list_notes(mock_read, capsys):
    list_notes()
    captured = capsys.readouterr()
    assert captured.out == "Listing notes...\n- Title (Due: 2025-01-09)\n"


@patch("actions.list_notes.read_json", side_effect=mock_read_json)
def test_empty_list_notes(mock_read, capsys):
    global mock_notes_storage
    mock_notes_storage = {}
    list_notes()
    captured = capsys.readouterr()
    assert captured.out == "Listing notes...\nNothing to list.\n"


@patch("actions.list_notes.read_json", side_effect=mock_read_json)
def test_no_due_date_list_notes(mock_read, capsys):
    global mock_notes_storage
    mock_notes_storage = {"Title": {"content": "Content", "due_date": None}}
    list_notes()
    captured = capsys.readouterr()
    assert captured.out == "Listing notes...\n- Title (Due: None)\n"


@patch("actions.list_notes.read_json", side_effect=mock_read_json)
def test_multiple_line_list_nodes(mock_read, capsys):
    global mock_notes_storage
    mock_notes_storage = {"Title": {"content": "Content", "due_date": "2025-01-09"},
                          "Title2": {"content": "Content2", "due_date": ""}}
    list_notes()
    captured = capsys.readouterr()
    assert captured.out == "Listing notes...\n- Title (Due: 2025-01-09)\n- Title2 (Due: None)\n"