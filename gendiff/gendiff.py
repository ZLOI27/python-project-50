import json

import yaml

from gendiff.cli import parse_args


def main() -> None:
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file))


def read_file(path: str):
    if path.endswith('.json'):
        load_data = json.load
    elif path.endswith(('.yaml', '.yml')):
        load_data = yaml.safe_load
    else:
        raise ValueError(f"ERROR: Unsupported format of file {path}.")
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            return load_data(file)
    except OSError as error:
        raise OSError(f"ERROR: Can't read file {path}. Reason: {error}")


def get_list_of_dict_with_sign(data1, data2) -> list:
    result = [
        {'key': key, 'sign': ' ', 'value': value}
        if (key in data2) and (value == data2[key])
        else {'key': key, 'sign': '-', 'value': value}
        for key, value in data1.items()
    ]
    result.extend([
        {'key': key, 'sign': '+', 'value': value}
        for key, value in data2.items()
        if (key not in data1) or value != data1[key]
    ])
    return result


def sort_list(items: list):
    def sort_by_rule(item: dict) -> tuple:
        """The sign -> digit for correctly sort items with the same key."""
        sign_order = {'-': 0, '+': 1, ' ': 2}
        return (item['key'], sign_order[item['sign']])
    items.sort(key=sort_by_rule)
    return items


def make_str_from_list(items: list) -> str:
    """
    Type checking for the output of strings without quotes,
    and for the correct output of True, False in the form of true, false.
    Doesn't matter for .yaml.
    """
    list_of_str = ['{']
    for item in items:
        sign = item['sign']

        if isinstance(item['key'], str):
            key = item['key']
        else:
            key = json.dumps(item['key'])

        if isinstance(item['value'], str):
            value = item['value']
        else:
            value = json.dumps(item['value'])

        list_of_str.append(f"  {sign} {key}: {value}")
    list_of_str.append('}')
    return '\n'.join(list_of_str)


def generate_diff(path1, path2) -> str:
    dict_data1 = read_file(path1)
    dict_data2 = read_file(path2)
    list_of_dict = get_list_of_dict_with_sign(dict_data1, dict_data2)
    sorted_list = sort_list(list_of_dict)
    return make_str_from_list(sorted_list)
