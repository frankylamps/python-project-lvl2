#!/usr/bin/env python3

import json
from gendiff.tools.gendiff_tool import generate_diff


def gendiff_func(path1, path2):
    """Compare two json files and get the difference."""  # noqa:  DAR101
    d1 = json.load(open(path1))  # noqa: WPS515
    d2 = json.load(open(path2))  # noqa: WPS515
    print(generate_diff(d1, d2))
