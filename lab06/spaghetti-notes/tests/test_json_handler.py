import os
import json
import pytest
from unittest.mock import mock_open, patch
from actions.json_handler import read_json, write_json


# Test read_json function
@patch("actions.json_handler.open", new_callable=mock_open, read_data='{"key": "value"}')
@patch("actions.json_handler.os.path.exists", return_value=True)
def test_read_json_success(mock_exists, mock_open_file):
    result = read_json("test.json")
    assert result == {"key": "value"}
    mock_open_file.assert_called_once_with("test.json", "r", encoding="utf-8")


@patch("actions.json_handler.open", new_callable=mock_open, read_data='')
@patch("actions.json_handler.os.path.exists", return_value=True)
def test_read_json_empty_file(mock_exists, mock_open_file, capsys):
    result = read_json("test.json")
    captured = capsys.readouterr()
    assert result == {}
    mock_open_file.assert_called_once_with("test.json", "r", encoding="utf-8")
    assert captured.out == "Error: Failed to decode JSON from test.json.\nExpecting value: line 1 column 1 (char 0)\n"


@patch("actions.json_handler.os.path.exists", return_value=False)
def test_read_json_file_not_exists(mock_exists):
    result = read_json("test.json")
    assert result == {}


# Test write_json function
@patch("actions.json_handler.open", new_callable=mock_open)
def test_write_json_success(mock_open_file):
    data = {"key": "value"}
    write_json(data, "test.json")

    # Assert the file was written with the correct data
    mock_open_file.assert_called_once_with("test.json", "w", encoding="utf-8")
    mock_open_file().write.assert_called_once_with(json.dumps(data))
