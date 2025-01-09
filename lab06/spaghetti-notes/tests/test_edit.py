import pytest
from unittest.mock import patch
from actions.edit import edit


# A pytest fixture to reset the in-memory storage
@pytest.fixture(autouse=True)
def reset_mock_storage():
    global mock_notes_storage
    mock_notes_storage = {"Title": {"content": "Content", "due_date": "2025-01-09"}}


# An in-memory dictionary to simulate the JSON storage
mock_notes_storage = {}


def mock_read_json():
    """Simulates reading from a JSON file."""
    return mock_notes_storage


def mock_write_json(data):
    """Simulates writing to a JSON file."""
    global mock_notes_storage
    mock_notes_storage = data


@patch("actions.edit.read_json", side_effect=mock_read_json)
@patch("actions.edit.write_json", side_effect=mock_write_json)
def test_edit_note_success(mock_read, mock_write):
    title = "Title"
    content = "This is the content of edit note success test"
    due_date = "1899-01-09"

    edit(title, content, due_date)
    notes = mock_read_json()

    assert title in notes
    assert notes[title]["content"] == content
    assert notes[title]["due_date"] == due_date


@patch("actions.edit.read_json", side_effect=mock_read_json)
@patch("actions.edit.write_json", side_effect=mock_write_json)
def test_edit_note_not_found(mock_read, mock_write):
    title = "Not Found Title"
    content = "This is the content of edit note not found test"
    due_date = "1899-01-09"

    edit(title, content, due_date)
    notes = mock_read_json()

    assert len(notes) == 1
    assert title not in notes
    assert "Title" in notes
    assert notes["Title"]["content"] == "Content"
    assert notes["Title"]["due_date"] == "2025-01-09"


@patch("actions.edit.read_json", side_effect=mock_read_json)
@patch("actions.edit.write_json", side_effect=mock_write_json)
def test_edit_no_content(mock_read, mock_write):
    title = "Title"
    content = None
    due_date = "1899-01-09"

    edit(title, content, due_date)
    notes = mock_read_json()

    assert title in notes
    assert notes[title]["content"] == "Content"
    assert notes[title]["due_date"] == due_date


@patch("actions.edit.read_json", side_effect=mock_read_json)
@patch("actions.edit.write_json", side_effect=mock_write_json)
def test_edit_no_change_due_date(mock_read, mock_write):
    title = "Title"
    content = "This is the content of edit note no due date test"
    due_date = None

    edit(title, content, due_date)
    notes = mock_read_json()

    assert title in notes
    assert notes[title]["content"] == content
    assert notes[title]["due_date"] == "2025-01-09"


@patch("actions.edit.read_json", side_effect=mock_read_json)
@patch("actions.edit.write_json", side_effect=mock_write_json)
def test_edit_non_due_date(mock_read, mock_write):
    title = "Title"
    content = "This is the content of edit note non due date test"
    due_date = "none"

    edit(title, content, due_date)
    notes = mock_read_json()

    assert title in notes
    assert notes[title]["content"] == content
    assert notes[title]["due_date"] is None


@patch("actions.edit.read_json", side_effect=mock_read_json)
@patch("actions.edit.write_json", side_effect=mock_write_json)
def test_no_change_edit(mock_read, mock_write, capsys):
    title = "Title"
    content = None
    due_date = None

    edit(title, content, due_date)
    captured = capsys.readouterr()
    notes = mock_read_json()

    assert title in notes
    assert notes[title]["content"] == "Content"
    assert notes[title]["due_date"] == "2025-01-09"
    assert captured.out == "No content or due date provided - no changes made to the note.\n"
