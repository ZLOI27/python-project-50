from gendiff.cli import parse_args
from gendiff.formatters.json_format import format_output_json
from gendiff.formatters.plain import format_output_plain
from gendiff.formatters.stylish import format_output_stylish
from gendiff.scripts.utils import read_file


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
    match format_name:
        case 'stylish':
            return format_output_stylish(sorted_diff)
        case 'plain':
            return format_output_plain(sorted_diff)
        case 'json':
            return format_output_json(sorted_diff)
        case _:
            print("Wrong format: {format_name}")


def main() -> None:
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
