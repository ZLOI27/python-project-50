import argparse


def parse_args(args=None):
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        epilog='Hi, Lyova!)'
    )

    parser.add_argument(
        '-f', '--format', type=str,
        default='stylish',
        help='set format of output'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    return parser.parse_args(args)
