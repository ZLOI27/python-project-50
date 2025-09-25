import json


def make_str_from_dict(items: dict, enclose=0) -> str:
    indent = '    ' * enclose
    list_of_str = ['{']
    for key, value in items.items():
        if not isinstance(key, str):
            key = json.dumps(key)
            
        if isinstance(value, dict):
            value = make_str_from_dict(value, enclose + 1)

        if not isinstance(value, str):
            value = json.dumps(value)

        list_of_str.append(f"{indent}    {key}: {value}")
    list_of_str.append(f"{indent}}}")
    return '\n'.join(list_of_str)


def make_str_from_list(items: list, format_name, enclose=0) -> str:
    """
    Type checking for the output of strings without quotes,
    and for the correct output of True, False in the form of true, false.
    Doesn't matter for .yaml.
    """
    if format_name != 'stylish':
        return "format {format_name} unsupported"
    indent = '    ' * enclose
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
            value = make_str_from_list(item['value'], format_name, enclose + 1)
        elif isinstance(item['value'], dict):
            value = make_str_from_dict(item['value'], enclose + 1)
        else:
            value = json.dumps(item['value'])

        list_of_str.append(f"{indent}  {sign} {key}: {value}")
    list_of_str.append(f"{indent}}}")
    return '\n'.join(list_of_str)