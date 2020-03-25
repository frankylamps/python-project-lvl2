#!/usr/bin/env python3

from gendiff.parsers.parsers import get_first_file
from gendiff.parsers.parsers import get_second_file


def engine(comparing_tool, comparing_files, rendering_tool):  # noqa: D103
    return rendering_tool(comparing_tool(
        get_first_file(comparing_files),
        get_second_file(comparing_files),
    ))
