import json

import yaml

from gendiff.cli import parse_args
from gendiff.views import make_str_from_list


def read_file(path: str):
    try:
        if path.endswith('.json'):
            load_data = json.load
        elif path.endswith(('.yaml', '.yml')):
            load_data = yaml.safe_load
        else:
            raise ValueError

        with open(path, mode='r', encoding='utf-8') as file:
            return load_data(file)
    except OSError as error:
        print(f"ERROR: Can't read file {path}. Reason: {error}")
        return None
    except ValueError:
        print(f"ERROR: Unsupported format of file {path}.")
        return None


def sort_list(items: list):
    def sort_by_rule(item: dict) -> tuple:
        """The sign -> digit for correctly sort items with the same key."""
        sign_order = {'-': 0, '+': 1, ' ': 2}
        return (item['key'], sign_order[item['sign']])
    items.sort(key=sort_by_rule)
    return items


def get_list_of_dict(data1, data2) -> list:
    if data1 == data2:
        return data1
    result = [
        {
            'key': key,
            'sign': ' ',
            'value': get_list_of_dict(value, data2[key])
        }
        if key in data2 and (
            (value == data2[key]) or
            (value != data2[key]) and
            (isinstance(value, dict) and isinstance(data2[key], dict))
        )
        else {
            'key': key,
            'sign': '-',
            'value': value
        }
        for key, value in data1.items()
    ]
    result.extend([
        {
            'key': key,
            'sign': '+',
            'value': value
        }
        for key, value in data2.items()
        if (
            (key not in data1) or
            (key in data1 and value != data1[key]) and
            (not isinstance(value, dict) or not isinstance(data2[key], dict))
        )
    ])
    return sort_list(result)


def generate_diff(path1, path2, format_name='stylish') -> str:
    dict_data1 = read_file(path1)
    dict_data2 = read_file(path2)
    sorted_list_of_dict = get_list_of_dict(dict_data1, dict_data2)
    return make_str_from_list(sorted_list_of_dict, format_name)


def main() -> None:
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
