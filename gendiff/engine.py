#!/usr/bin/env python3
from gendiff.parsers.parsers import get_first_file
from gendiff.parsers.parsers import get_second_file


def engine(comparing_tool, comparing_files):
    """
    Apply comparing tool to 2  comparing files.

    Args:
        comparing_tool (func): tool, that compares two json files
        comparing_files (func): parser with two files set with get_files() func

    Returns:
        string (str): result if the tools applied to files
    """

    return comparing_tool(
        get_first_file(comparing_files),
        get_second_file(comparing_files),
    )
