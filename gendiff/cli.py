import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        epilog='Hi, Lyova Parsyan!)'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.parse_args()
