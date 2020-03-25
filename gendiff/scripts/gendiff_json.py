#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.parsers.parsers import make_json_files
from gendiff.tools.gendiff_tool import gen_diff
from gendiff.tools.rendering_tool import render


def main():
    """Print difference between two files."""
    engine(
        gen_diff,
        make_json_files(),
        render,
    )


if __name__ == '__main__':
    main()
