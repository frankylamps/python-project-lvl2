#!/usr/bin/env python3

import argparse
import json


def engine(tool, f1='', f2=''):
    """
    Apply tool to 2  arguments given in terminal.

    Args:
        tool (str): tool, that compares two json files
    """
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str, default=f1, nargs='?')
    parser.add_argument('second_file', type=str, default=f2, nargs='?')
    parser.add_argument(
        '-f', '--format', metavar='FORMAT', help='set format of output',
    )

    args = parser.parse_args()

    d1 = json.load(open(args.first_file))  # noqa: WPS515
    d2 = json.load(open(args.second_file))  # noqa: WPS515

    print(tool(d1, d2))
