import pytest
from typing import List
from unittest.mock import patch, mock_open
from pathlib import Path

@pytest.fixture()
def file_path() -> Path:
    return Path(__file__).parent / "inventory/inventory.json"


@pytest.fixture()
def file_device_json_content(file_path) -> str:
    file = open(file_path)
    raw_devices = file.read()
    file.close()
    return raw_devices

@pytest.fixture()
def mock_file(file_path: Path, file_device_json_content: str):
    with open(file_path) as f:
        with patch("builtins.open", return_value=f) as mock_file:
            yield mock_file


# @pytest.fixture()
# def file_path() -> Path:
#     return Path(__file__).parent.absolute() / "fixtures/example.txt"

# @pytest.fixture()
# def file_content(file_path) -> str:
#     file = open(file_path)
#     content = file.read()
#     #file.close()
#     return content

# @pytest.fixture()
# def file_lines(file_content: str) -> List[str]:
#     return file_content.splitlines()

# @pytest.fixture()
# def reverse_file_lines(file_lines: List[str]) -> List[str]:
#     return file_lines[::-1]

# @pytest.fixture()
# def mock_file(file_path: Path, file_content: str):
#     with open(file_path) as f:
#         with patch("builtins.open", return_value=f) as mock_file:
#             yield mock_file
