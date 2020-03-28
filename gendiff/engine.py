#!/usr/bin/env python3

from gendiff.parsers.parsers import get_first_file
from gendiff.parsers.parsers import get_second_file
from gendiff.parsers.parsers import get_format


def engine(
    comparing_tool,
    comparing_files,
    rendering_tool,
    comparing_tool_plain,
    rendering_tool_plain,
    ):  # noqa: D103
    if get_format(comparing_files) == 'plain':
        return rendering_tool_plain(comparing_tool_plain(
            get_first_file(comparing_files),
            get_second_file(comparing_files),
        ))
    return rendering_tool(comparing_tool(
        get_first_file(comparing_files),
        get_second_file(comparing_files),
    ))
