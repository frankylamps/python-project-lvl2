import json
import yaml
import sys
import argparse


def make_json_files(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, default=None, nargs='?')
    parser.add_argument('second_file', type=str, default=None, nargs='?')
    parser.add_argument(
        '-f', '--format', metavar='FORMAT', help='set format of output',
    )

    paths = parser.parse_args(args)

    return {
        'first file': json.load(open(paths.first_file)),
        'second file': json.load(open(paths.second_file)),
        'format': paths.format,
    }


def make_yaml_files(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, default=None, nargs='?')
    parser.add_argument('second_file', type=str, default=None, nargs='?')
    parser.add_argument(
        '-f', '--format', metavar='FORMAT', help='set format of output',
    )

    paths = parser.parse_args(args)

    return {
        'first file': yaml.load(
            (open(paths.first_file, 'r')),
            Loader=yaml.SafeLoader,
        ),
        'second file': yaml.load(
            (open(paths.second_file, 'r')),
            Loader=yaml.SafeLoader,
        ),
        'format': paths.format,
    }


def get_first_file(files):
    return files.get('first file')


def get_second_file(files):
    return files.get('second file')


def get_format(files):
    return files.get('format')
