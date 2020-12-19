import argparse
from gendiff import format


def formatter(name):
    if name == format.JSON:
        return format.json
    elif name == format.PLAIN:
        return format.plain
    elif name == format.DEFAULT:
        return format.default
    raise argparse.ArgumentTypeError(
        'Unknown formatter: {}'.format(name)
    )


def take_arguments():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('path_to_file1')
    parser.add_argument('path_to_file2')
    parser.add_argument(
        '-f', '--format',
        default=format.DEFAULT,
        help='set format of output',
        type=formatter,  # Doen's work with choices=format.FORMATTERS
    )
    return parser
