import json


def get_value(value):
    if isinstance(value, (dict, list)):
        value = "[complex value]"
    elif isinstance(value, str):
        value = f"'{value}'"
    else:
        value = json.dumps(value)
    return value


def format_output_plain(diff: list, accum=None, result=None):
    if result is None:
        result = []
    if accum is None:
        accum = ["Property '"]
    for item in diff:
        value = get_value(item['value'])

        match item['status']:
            case 'unchanged':
                continue
            case 'nested':
                accum.append(f"{item['key']}.")
                format_output_plain(item['value'], accum, result)
            case 'removed':
                accum.append(f"{item['key']}' was removed")
                result.append(''.join(accum))
            case 'added':
                accum.append(f"{item['key']}' was added with value: {value}")
                result.append(''.join(accum))
            case 'changed':
                new_value = get_value(item['new_value'])
                accum.append(
                    f"{item['key']}' was updated. From {value} to {new_value}"
                )
                result.append(''.join(accum))
        accum.pop()
    
    return '\n'.join(result)
