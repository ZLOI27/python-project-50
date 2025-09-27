import os

from gendiff.gendiff import generate_diff, read_file

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
    file1_json = os.path.join(dir_with_data, 'file1.json')
    file2_json = os.path.join(dir_with_data, 'file2.json')
    file1_yaml = os.path.join(dir_with_data, 'file1.yaml')
    file2_yaml = os.path.join(dir_with_data, 'file2.yaml')
    assert read_file(file1_json) == right_data1
    assert read_file(file1_json) != right_data2
    assert read_file(file2_json) == right_data2
    assert read_file(file2_json) != right_data1
    assert read_file(file1_yaml) == right_data1
    assert read_file(file1_yaml) != right_data2
    assert read_file(file2_yaml) == right_data2
    assert read_file(file2_yaml) != right_data1


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

    test_file_path = os.path.join(dir_with_data, 'test_result_plain.txt')
    try:
        with open(test_file_path, 'r', encoding='utf-8') as file:
            right_data_plain = file.read()
    except OSError:
        print('Can not open test_file.')

    wrong_str = ''
    file1_json = os.path.join(dir_with_data, 'file1.json')
    file2_json = os.path.join(dir_with_data, 'file2.json')
    file1_yaml = os.path.join(dir_with_data, 'file1.yaml')
    file2_yaml = os.path.join(dir_with_data, 'file2.yaml')

    file3_json = os.path.join(dir_with_data, 'file3.json')
    file4_json = os.path.join(dir_with_data, 'file4.json')
    file3_yaml = os.path.join(dir_with_data, 'file3.yaml')
    file4_yaml = os.path.join(dir_with_data, 'file4.yaml')

    assert generate_diff(file1_json, file2_json) == right_str
    assert generate_diff(file1_json, file2_json) != wrong_str
    assert generate_diff(file1_yaml, file2_yaml) == right_str
    assert generate_diff(file1_yaml, file2_yaml) != wrong_str

    assert generate_diff(file3_json, file4_json) == right_data
    assert generate_diff(file3_json, file4_json) != wrong_str
    assert generate_diff(file3_yaml, file4_yaml) == right_data
    assert generate_diff(file3_yaml, file4_yaml) != wrong_str

    assert generate_diff(file3_json, file4_json, 'plain') == right_data_plain
    assert generate_diff(file3_json, file4_json, 'plain') != wrong_str
    assert generate_diff(file3_yaml, file4_yaml, 'plain') == right_data_plain
    assert generate_diff(file3_yaml, file4_yaml, 'plain') != wrong_str

