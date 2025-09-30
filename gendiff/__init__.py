from gendiff.cli import parse_args
from gendiff.core.gendiff import generate_diff, main
from gendiff.io.utils import read_file

__all__ = [
    'parse_args',
    'generate_diff',
    'read_file',
    'main',
]