import json


def make_str_from_dict(items: dict, indent=0) -> str:
    indent_str = ' ' * indent
    list_of_str = ['{']
    for key, value in items.items():
        if not isinstance(key, str):
            key = json.dumps(key)
            
        if isinstance(value, dict):
            value = make_str_from_dict(value, indent + 4)

        if not isinstance(value, str):
            value = json.dumps(value)

        list_of_str.append(f"{indent_str}    {key}: {value}")
    list_of_str.append(f"{indent_str}}}")
    return '\n'.join(list_of_str)


def get_key(item_key):
    if isinstance(item_key, str):
        key = item_key
    else:
        key = json.dumps(item_key)
    return key


def get_value(value, status, indent):
    if status == 'nested':
        result = format_output_stylish(value, indent + 4)
    elif isinstance(value, dict):
        result = make_str_from_dict(value, indent + 4)
    elif isinstance(value, str):
        result = value
    else:
        result = json.dumps(value)
    return result


def format_output_stylish(diff: list, indent=0) -> str:
    """
    Type checking for the output of strings without quotes,
    and for the correct output of True, False in the form of true, false.
    Doesn't matter for .yaml.
    """
    indent_str = ' ' * indent
    sign = {
        'removed': '-',
        'added': '+',
        'unchanged': ' ',
        'nested': ' ',
        'changed': '-',
    }
    list_of_str = ['{']
    for item in diff:
        status = item['status']
        key = get_key(item['key'])
        value = get_value(item['value'], status, indent)
        list_of_str.append(f"{indent_str}  {sign[status]} {key}: {value}")
        if status == 'changed':
            new_value = get_value(item['new_value'], status, indent)
            list_of_str.append(
                f"{indent_str}  {sign['added']} {key}: {new_value}"
            )
            
    list_of_str.append(f"{indent_str}}}")
    return '\n'.join(list_of_str)