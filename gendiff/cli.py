import argparse


def take_arguments():
    """Take arguments from command line or list and return as dict.

    Args:
        args: first path to file, second path to file, format (optional)

    Returns:
        dictionaty with provided paths and format (optional)
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_path_to_file')
    parser.add_argument('second_path_to_file')
    parser.add_argument(
        '-f',
        '--format',
        default='nested',
        metavar='FORMAT',
        choices=['nested', 'plain', 'json'],
        help='set format of output',
    )

    paths = parser.parse_args()

    return {
        'first path': paths.first_path_to_file,
        'second path': paths.second_path_to_file,
        'format': paths.format,
    }
