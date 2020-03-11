#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.tools.gendiff_tool import generate_diff


def main():
    """Print string with difference between two files."""
    print(engine(generate_diff))


if __name__ == '__main__':
    main()
