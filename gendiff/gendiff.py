import json

import yaml

from gendiff.cli import parse_args
from gendiff.views.plain import format_output_plain
from gendiff.views.stylish import format_output_stylish


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


def get_diff(data1, data2) -> list:
    if data1 == data2:
        return data1
    diff = []
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    for key in keys:
        if key not in data2:
            diff.append({
                'key': key,
                'status': 'removed',
                'value': data1[key],
            })
        elif key not in data1:
            diff.append({
                'key': key,
                'status': 'added',
                'value': data2[key],
            })
        elif data1[key] == data2[key]:
            diff.append({
                'key': key,
                'status': 'unchanged',
                'value': data1[key],
            })
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'status': 'nested',
                'value': get_diff(data1[key], data2[key]),
            })
        else:
            diff.append({
                'key': key,
                'status': 'changed',
                'value': data1[key],
                'new_value': data2[key],
            })
            
    diff.sort(key=lambda item: item['key'])
    return diff


def generate_diff(path1, path2, format_name='stylish') -> str:
    dict_data1 = read_file(path1)
    dict_data2 = read_file(path2)
    sorted_diff = get_diff(dict_data1, dict_data2)
    if format_name == 'stylish':
        return format_output_stylish(sorted_diff)
    elif format_name == 'plain':
        return format_output_plain(sorted_diff)


def main() -> None:
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
