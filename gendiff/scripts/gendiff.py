#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.tools.gendiff_tools import generate_diff
from gendiff.tools.gendiff_tools import get_files


def main():
    """Print difference between two files."""
    print(engine(generate_diff, get_files()))


if __name__ == '__main__':
    main()
