import json

import yaml


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
