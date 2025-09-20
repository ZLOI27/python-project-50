import json

from gendiff.cli import parse_args


def main() -> None:
    args = parse_args()
    data1 = read_file_json(args.first_file)
    data2 = read_file_json(args.second_file)
    # result = compare_data_from_files(data1, data2)
    print(data1, data2)


def read_file_json(path: str):
    try:
        with open(path, mode='r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as error:
        print("Can't read_file_json\n", error)
        return None


def compare_data_from_files(data1: dict, data2: dict):
    pass
