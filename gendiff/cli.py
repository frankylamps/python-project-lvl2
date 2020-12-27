import argparse
from gendiff import format


def take_arguments():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('path_to_file1')
    parser.add_argument('path_to_file2')
    parser.add_argument(
        '-f', '--format',
        default=format.DEFAULT,
        help='set format of output',
        type=format.formatter,  # Doen's work with choices=format.FORMATTERS
    )
    return parser
