import sys
import argparse


def take_arguments(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, default=None, nargs='?')
    parser.add_argument('second_file', type=str, default=None, nargs='?')
    parser.add_argument(
        '-f', '--format', metavar='FORMAT', help='set format of output',
    )

    paths = parser.parse_args(args)

    return {
        'first file': paths.first_file,
        'second file': paths.second_file,
        'format': paths.format,
    }


def get_first_file(files):
    return files.get('first file')


def get_second_file(files):
    return files.get('second file')


def get_format(files):
    return files.get('format')
