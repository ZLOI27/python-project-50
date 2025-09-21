from gendiff.cli import parse_args


def test_parse_args_with_args():
    test_args = ['--format', 'test_format', 'file1.json', 'file2.json']

    args = parse_args(test_args)

    assert args.format == 'test_format'
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'