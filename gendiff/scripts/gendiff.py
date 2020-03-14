#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.tools.gendiff_tool import generate_diff


def main(f1='', f2=''):
    """Print string with difference between two files."""
    engine(generate_diff, f1, f2)


if __name__ == '__main__':
    main()
