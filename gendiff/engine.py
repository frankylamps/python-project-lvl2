#!/usr/bin/env python3

from gendiff.parsers.parsers import get_first_file
from gendiff.parsers.parsers import get_second_file
from gendiff.parsers.parsers import get_format
import yaml
import json


def engine(
    comparing_tool,
    comparing_files,
    rendering_tool,
    comparing_tool_plain,
    rendering_tool_plain,
    ):  # noqa: D103
    path_one = get_first_file(comparing_files)
    path_two = get_second_file(comparing_files)
    file_one = None
    file_two = None
    if path_one[path_one.index('.') + 1:] == 'yaml':
        if path_two[path_two.index('.') + 1:] == 'yaml':
            file_one = yaml.load((open(path_one, 'r')), Loader=yaml.SafeLoader)
            file_two = yaml.load((open(path_two, 'r')), Loader=yaml.SafeLoader)

    if path_one[path_one.index('.') + 1:] == 'json':
        if path_two[path_two.index('.') + 1:] == 'json':
            file_one = json.load(open(path_one))
            file_two = json.load(open(path_two))

    if get_format(comparing_files) == 'plain':
        return rendering_tool_plain(comparing_tool_plain(
            file_one,
            file_two,
        ))
    return rendering_tool(comparing_tool(
        file_one,
        file_two,
    ))
