import json


def format_output_json(diff: list):
    return json.dumps(diff, indent=2, ensure_ascii=False)