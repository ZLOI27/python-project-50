from gendiff.core import generate_diff, read_file_json, sort_list

path1 = '/home/zk/python-project-50/file1.json'
data1 = {
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False
}

path2 = '/home/zk/python-project-50/file2.json'
data2 = {
    "timeout": 20,
    "verbose": True,
    "host": "hexlet.io"
}


def test_read_file_json():
    assert read_file_json(path1) == data1

    assert read_file_json(path2) == data2


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


def test_generate_diff():
    right_str = ("{\n"
    "  - follow: false\n"
    "    host: hexlet.io\n"
    "  - proxy: 123.234.53.22\n"
    "  - timeout: 50\n"
    "  + timeout: 20\n"
    "  + verbose: true\n"
    "}")
    assert generate_diff(path1, path2) == right_str