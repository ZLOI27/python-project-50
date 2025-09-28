import os

from gendiff.io_utils import read_file

current_dir = os.path.dirname(os.path.abspath(__file__))
dir_with_data = os.path.join(current_dir, 'test_data')

right_data1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

right_data2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}


def test_read_file():
    file1_json_path = os.path.join(dir_with_data, 'file1.json')
    file2_json_path = os.path.join(dir_with_data, 'file2.json')
    file1_yaml_path = os.path.join(dir_with_data, 'file1.yaml')
    file2_yaml_path = os.path.join(dir_with_data, 'file2.yaml')

    assert read_file(file1_json_path) == right_data1
    assert read_file(file1_json_path) != right_data2
    assert read_file(file2_json_path) == right_data2
    assert read_file(file2_json_path) != right_data1
    assert read_file(file1_yaml_path) == right_data1
    assert read_file(file1_yaml_path) != right_data2
    assert read_file(file2_yaml_path) == right_data2
    assert read_file(file2_yaml_path) != right_data1