import pytest
from unittest.mock import patch
from actions.delete import delete


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


def mock_write_json(data):
    """Simulates writing to a JSON file."""
    global mock_notes_storage
    mock_notes_storage = data


@patch("actions.delete.read_json", side_effect=mock_read_json)
@patch("actions.delete.write_json", side_effect=mock_write_json)
def test_found_title_delete(mock_read, mock_write):
    title = "Title"

    delete(title)
    notes = mock_read_json()

    assert title not in notes
    assert len(notes) == 0


@patch("actions.delete.read_json", side_effect=mock_read_json)
@patch("actions.delete.write_json", side_effect=mock_write_json)
def test_not_found_title_delete(mock_read, mock_write):
    actual_title = "Title"
    title = "Not Found Title"

    delete(title)
    notes = mock_read_json()

    assert len(notes) == 1
    assert title not in notes
    assert "Title" in notes
    assert notes[actual_title]["content"] == "Content"
    assert notes[actual_title]["due_date"] == "2025-01-09"