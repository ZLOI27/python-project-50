import os
import tempfile

import pytest

from gendiff.cli import parse_args
from gendiff.gendiff import generate_diff, read_file_json, sort_list


@pytest.fixture
def temp_dir_with_files():
    with tempfile.TemporaryDirectory() as temp_dir:
        file1_path = os.path.join(temp_dir, 'file1.json')
        file2_path = os.path.join(temp_dir, 'file2.json')

        with open(file1_path, 'w') as f:
            f.write('{\n'
            '"host": "hexlet.io",\n'
            '"timeout": 50,\n'
            '"proxy": "123.234.53.22",\n'
            '"follow": false\n'
            '}')
        with open(file2_path, 'w') as f:
            f.write('{\n'
            '"timeout": 20,\n'
            '"verbose": true,\n'
            '"host": "hexlet.io"\n'
            '}')

        yield temp_dir


data1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

data2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}


def test_read_file_json(temp_dir_with_files):
    file1_path = os.path.join(temp_dir_with_files, 'file1.json')
    file2_path = os.path.join(temp_dir_with_files, 'file2.json')
    assert read_file_json(file1_path) == data1

    assert read_file_json(file2_path) == data2


def test_sort_list():
    lst = [
    {'key': 'qwe', 'sign': '+', 'value': 3},
    {'key': 'abc', 'sign': ' ', 'value': 3},
    {'key': 'qwe', 'sign': '-', 'value': 3},
    ]
    assert sort_list(lst) == [
        {'key': 'abc', 'sign': ' ', 'value': 3},
        {'key': 'qwe', 'sign': '-', 'value': 3},
        {'key': 'qwe', 'sign': '+', 'value': 3},
    ]


def test_generate_diff(temp_dir_with_files):
    right_str = ("{\n"
    "  - follow: false\n"
    "    host: hexlet.io\n"
    "  - proxy: 123.234.53.22\n"
    "  - timeout: 50\n"
    "  + timeout: 20\n"
    "  + verbose: true\n"
    "}")
    file1_path = os.path.join(temp_dir_with_files, 'file1.json')
    file2_path = os.path.join(temp_dir_with_files, 'file2.json')
    assert generate_diff(file1_path, file2_path) == right_str


def test_parse_args_with_args():
    test_args = ['--format', 'test_format', 'file1.json', 'file2.json']

    args = parse_args(test_args)

    assert args.format == 'test_format'
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'