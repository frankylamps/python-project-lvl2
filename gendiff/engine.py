#!/usr/bin/env python3

from gendiff.tools.gendiff_tools import get_new_file
from gendiff.tools.gendiff_tools import get_old_file


def engine(tool, parser):
    """
    Apply tool to 2  arguments given in terminal or in function.

    Args:
        tool (str): tool, that compares two json files
    """

    d1 = get_old_file(parser)
    d2 = get_new_file(parser)

    return tool(d1, d2)
