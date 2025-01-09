import pytest
from unittest.mock import patch
from actions.view import view


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


@patch("actions.view.read_json", side_effect=mock_read_json)
def test_view(mock_read, capsys):
    view("Title")
    captured = capsys.readouterr()
    assert captured.out == "Title\n---\nContent\n---\nDue:2025-01-09\n"


@patch("actions.view.read_json", side_effect=mock_read_json)
def test_not_found_view(mock_read, capsys):
    view("Not Found Title")
    captured = capsys.readouterr()
    assert captured.out == "Doesn't exist.\n"


@patch("actions.view.read_json", side_effect=mock_read_json)
def test_no_due_date_view(mock_read, capsys):
    global mock_notes_storage
    mock_notes_storage = {"Title": {"content": "Content", "due_date": None}}
    view("Title")
    captured = capsys.readouterr()
    assert captured.out == "Title\n---\nContent\n---\nNo due date.\n"
