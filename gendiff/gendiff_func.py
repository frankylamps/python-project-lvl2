#!/usr/bin/env python3

import json
from gendiff.tools.gendiff_tool import generate_diff


def gendiff_func(path1, path2):
    d1 = json.load(open(path1))
    d2 = json.load(open(path2))
    print(generate_diff(d1, d2))


