import json

from gendiff.cli import parse_args


def main() -> None:
    args = parse_args()
    print(generate_diff(args.first_file, args.second_file))


def read_file_json(path: str):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as error:
        print("Can't read_file_json\n", error)
        return None


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
    def sort_by_rule(item: dict) -> str:
        """The sign is changed to correctly sort items with the same key."""
        if item['sign'] == '+':
            sign = '-'
        elif item['sign'] == '-':
            sign = '+'
        else:
            sign = ' '
        return str([item['key'], sign])
    items.sort(key=sort_by_rule)
    return items


def make_str_from_list(items: list) -> str:
    """
    Type checking for the output of strings without quotes,
    and for the correct output of True, False in the form of true, false.
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
    data1 = read_file_json(path1)
    data2 = read_file_json(path2)
    sorted_list_of_dict = sort_list(get_list_of_dict_with_sign(data1, data2))
    return make_str_from_list(sorted_list_of_dict)
