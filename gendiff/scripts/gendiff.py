#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.tools.gendiff_tools import generate_diff
from gendiff.tools.gendiff_tools import parse_args


def main():
    """Print string with difference between two files."""
    print(engine(generate_diff, parse_args()))


if __name__ == '__main__':
    main()
