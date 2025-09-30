from gendiff.cli import parse_args
from gendiff.scripts.diff import generate_diff, main
from gendiff.scripts.utils import read_file

__all__ = [
    'parse_args',
    'generate_diff',
    'read_file',
    'main',
]