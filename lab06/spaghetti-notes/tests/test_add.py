import pytest
from unittest.mock import patch
from actions.add import add


# A pytest fixture to reset the in-memory storage
@pytest.fixture(autouse=True)
def reset_mock_storage():
    global mock_notes_storage
    mock_notes_storage = {}  # Reset the storage before each test


# An in-memory dictionary to simulate the JSON storage
mock_notes_storage = {}


def mock_read_json():
    """Simulates reading from a JSON file."""
    return mock_notes_storage


def mock_write_json(data):
    """Simulates writing to a JSON file."""
    global mock_notes_storage
    mock_notes_storage = data


@patch("actions.add.read_json", side_effect=mock_read_json)
@patch("actions.add.write_json", side_effect=mock_write_json)
def test_add_note_success(mock_read, mock_write):
    title = "Test Note"
    content = "This is the content of add note success test"
    due_date = "2025-01-09"

    add(title, content, due_date)
    notes = mock_read_json()

    assert title in notes
    assert notes[title]["content"] == content
    assert notes[title]["due_date"] == due_date


@patch("actions.add.read_json", side_effect=mock_read_json)
@patch("actions.add.write_json", side_effect=mock_write_json)
def test_add_existing_note(mock_read, mock_write):
    title = "Test Note"
    content = "This is the content of add existing note test"
    due_date = "2025-01-09"

    add(title, content, due_date)
    add(title, "Different Content", "2026-01-01")

    notes = mock_read_json()

    assert len(notes) == 1
    assert notes[title]["content"] == content
    assert notes[title]["due_date"] == due_date


@patch("actions.add.read_json", side_effect=mock_read_json)
@patch("actions.add.write_json", side_effect=mock_write_json)
def test_add_no_content(mock_read, mock_write):
    title = "Test Note"
    content = ""
    due_date = "2025-01-09"

    add(title, content, due_date)

    notes = mock_read_json()

    assert len(notes) == 0


@patch("actions.add.read_json", side_effect=mock_read_json)
@patch("actions.add.write_json", side_effect=mock_write_json)
def test_add_no_due_date(mock_read, mock_write):
    title = "Test Note"
    content = "Random Content"
    due_date = None

    add(title, content, due_date)

    notes = mock_read_json()

    assert title in notes
    assert notes[title]["content"] == content
    assert notes[title]["due_date"] is None
