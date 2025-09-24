import json

import yaml

from gendiff.cli import parse_args


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


def make_str_from_dict(items: dict, enclos=0) -> str:
    indent = '    ' * enclos
    list_of_str = ['{']
    for key, value in items.items():
        if not isinstance(key, str):
            key = json.dumps(key)
            
        if isinstance(value, dict):
            value = make_str_from_dict(value, enclos + 1)

        if not isinstance(value, str):
            value = json.dumps(value)

        list_of_str.append(f"{indent}    {key}: {value}")
    list_of_str.append(f"{indent}}}")
    return '\n'.join(list_of_str)


def make_str_from_list(items: list, enclos=0) -> str:
    """
    Type checking for the output of strings without quotes,
    and for the correct output of True, False in the form of true, false.
    Doesn't matter for .yaml.
    """
    indent = '    ' * enclos
    list_of_str = ['{']
    for item in items:
        sign = item['sign']

        if isinstance(item['key'], str):
            key = item['key']
        else:
            key = json.dumps(item['key'])

        if isinstance(item['value'], str):
            value = item['value']
        elif isinstance(item['value'], list):
            value = make_str_from_list(item['value'], enclos + 1)
        elif isinstance(item['value'], dict):
            value = make_str_from_dict(item['value'], enclos + 1)
        else:
            value = json.dumps(item['value'])

        list_of_str.append(f"{indent}  {sign} {key}: {value}")
    list_of_str.append(f"{indent}}}")
    return '\n'.join(list_of_str)


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


def generate_diff(path1, path2) -> str:
    dict_data1 = read_file(path1)
    dict_data2 = read_file(path2)
    sorted_list_of_dict = get_list_of_dict(dict_data1, dict_data2)
    return make_str_from_list(sorted_list_of_dict)


def main() -> None:
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file))
