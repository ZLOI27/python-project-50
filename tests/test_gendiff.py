import os

from gendiff.gendiff import generate_diff
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


def open_file(file_name: str) -> dict:
    test_file_path = os.path.join(dir_with_data, file_name)
    try:
        with open(test_file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except OSError:
        print('Can not open test_file.')


def test_generate_diff():
    right_data_stylish = open_file('test_result_stylish.txt')
    right_data_plain = open_file('test_result_plain.txt')
    # right_data_json = open_file('test_result_json.txt')
    wrong_str = ''
    
    file3_json = os.path.join(dir_with_data, 'file3.json')
    file4_json = os.path.join(dir_with_data, 'file4.json')
    file3_yaml = os.path.join(dir_with_data, 'file3.yaml')
    file4_yaml = os.path.join(dir_with_data, 'file4.yaml')

    assert generate_diff(file3_json, file4_json) == right_data_stylish
    assert generate_diff(file3_json, file4_json) != wrong_str
    assert generate_diff(file3_yaml, file4_yaml) == right_data_stylish
    assert generate_diff(file3_yaml, file4_yaml) != wrong_str

    assert generate_diff(file3_json, file4_json, 'plain') == right_data_plain
    assert generate_diff(file3_json, file4_json, 'plain') != wrong_str
    assert generate_diff(file3_yaml, file4_yaml, 'plain') == right_data_plain
    assert generate_diff(file3_yaml, file4_yaml, 'plain') != wrong_str

    # assert generate_diff(file3_json, file4_json, 'json') == right_data_json
    # assert generate_diff(file3_json, file4_json, 'json') != wrong_str
    # assert generate_diff(file3_yaml, file4_yaml, 'json') == right_data_json
    # assert generate_diff(file3_yaml, file4_yaml, 'json') != wrong_str
