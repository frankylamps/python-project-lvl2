#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.parsers.parsers import take_arguments
from gendiff.formatters.plain.gendiff_tool import make_plain_structures
from gendiff.formatters.nested.gendiff_tool import gen_nested_diff
from gendiff.formatters.plain.rendering_tool import render_plain
from gendiff.formatters.nested.rendering_tool import render_nested


def main():
    """Print difference between two files."""
    engine(
        gen_nested_diff,
        take_arguments(),
        render_nested,
        make_plain_structures,
        render_plain,
    )


if __name__ == '__main__':
    main()
