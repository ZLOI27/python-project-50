import os

from gendiff.gendiff import generate_diff, read_file, sort_list

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
    file1_path_json = os.path.join(dir_with_data, 'file1.json')
    file2_path_json = os.path.join(dir_with_data, 'file2.json')
    file1_path_yaml = os.path.join(dir_with_data, 'file1.yaml')
    file2_path_yaml = os.path.join(dir_with_data, 'file2.yaml')
    assert read_file(file1_path_json) == right_data1
    assert read_file(file1_path_json) != right_data2
    assert read_file(file2_path_json) == right_data2
    assert read_file(file2_path_json) != right_data1
    assert read_file(file1_path_yaml) == right_data1
    assert read_file(file1_path_yaml) != right_data2
    assert read_file(file2_path_yaml) == right_data2
    assert read_file(file2_path_yaml) != right_data1


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
    assert sort_list(lst) != [
        {'key': 'abc', 'sign': ' ', 'value': 3},
        {'key': 'qwe', 'sign': '+', 'value': 3},
        {'key': 'qwe', 'sign': '-', 'value': 3},
    ]


def test_generate_diff():
    right_str = ("{\n"
                "  - follow: false\n"
                "    host: hexlet.io\n"
                "  - proxy: 123.234.53.22\n"
                "  - timeout: 50\n"
                "  + timeout: 20\n"
                "  + verbose: true\n"
                "}")
    test_file_path = os.path.join(dir_with_data, 'test_result.txt')
    try:
        with open(test_file_path, 'r', encoding='utf-8') as file:
            right_data = file.read()
    except OSError:
        print('Can not open test_file.')

    wrong_str = ''
    print(right_data)
    file1_path_json = os.path.join(dir_with_data, 'file1.json')
    file2_path_json = os.path.join(dir_with_data, 'file2.json')
    file1_path_yaml = os.path.join(dir_with_data, 'file1.yaml')
    file2_path_yaml = os.path.join(dir_with_data, 'file2.yaml')

    file3_path_json = os.path.join(dir_with_data, 'file3.json')
    file4_path_json = os.path.join(dir_with_data, 'file4.json')
    file3_path_yaml = os.path.join(dir_with_data, 'file3.yaml')
    file4_path_yaml = os.path.join(dir_with_data, 'file4.yaml')

    assert generate_diff(file1_path_json, file2_path_json) == right_str
    assert generate_diff(file1_path_json, file2_path_json) != wrong_str
    assert generate_diff(file1_path_yaml, file2_path_yaml) == right_str
    assert generate_diff(file1_path_yaml, file2_path_yaml) != wrong_str

    assert generate_diff(file3_path_json, file4_path_json) == right_data
    assert generate_diff(file3_path_json, file4_path_json) != wrong_str
    assert generate_diff(file3_path_yaml, file4_path_yaml) == right_data
    assert generate_diff(file3_path_yaml, file4_path_yaml) != wrong_str

