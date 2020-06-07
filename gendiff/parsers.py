import sys
import argparse
import yaml
import json


def take_arguments(args=sys.argv[1:]):  # noqa: WPS404
    """Take arguments from command line or list and return as dict.

    Args:
        args: first path to file, second path to file, format (optional)

    Returns:
        dictionaty with provided paths and format (optional)
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_path_to_file')  # noqa: E501
    parser.add_argument('second_path_to_file')  # noqa: E501
    parser.add_argument(
        '-f', '--format', metavar='FORMAT', help='set format of output',
    )

    paths = parser.parse_args(args)

    return {
        'first path': paths.first_path_to_file,
        'second path': paths.second_path_to_file,
        'format': paths.format,
    }


def load_file(path):
    """Load json or yaml file and convert it to python dict.

    Args:
        path (str): path to file

    Returns:
        dict:
    """
    if path[path.rfind('.') + 1:] == 'yaml':
        return yaml.load((open(path, 'r')), Loader=yaml.SafeLoader)  # noqa: WPS515, E501
    if path[path.rfind('.') + 1:] == 'json':
        return json.load(open(path))  # noqa: WPS515
