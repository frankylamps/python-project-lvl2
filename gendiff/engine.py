#!/usr/bin/env python3

from gendiff.tools.gendiff_tools import get_new_file
from gendiff.tools.gendiff_tools import get_old_file


def engine(comparing_tool, comparing_files):
    """
    Apply comparing tool to 2  comparing files.

    Args:
        comparing_tool (func): tool, that compares two json files
        comparing_files (func): parser with two files set with get_files() func

    Returns:
        string (str): result if the tools applied to files
    """
    d1 = get_old_file(comparing_files)
    d2 = get_new_file(comparing_files)

    return comparing_tool(d1, d2)
