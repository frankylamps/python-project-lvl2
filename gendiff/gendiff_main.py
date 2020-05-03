#!/usr/bin/env python3


from gendiff.formatters.plain.rendering_and_gendiff_tool import render_and_gen_plain_diff  # noqa: E501
from gendiff.formatters.nested.gendiff_tool import gen_nested_diff
from gendiff.formatters.nested.rendering_tool import render_nested
from gendiff.formatters.json.rendering_tool import render_json
from gendiff.parsers.parsers import take_arguments
from gendiff.parsers.parsers import load_file


def gendiff(comparing_files_paths=None):
    """Compare two yaml ot json files and print the difference.

    Args:
        comparing_files_paths: 2 paths to files and format (optional)

    Returns:
        Nothing, just print out the difference between 2 files
    """
    if not comparing_files_paths:
        comparing_files_paths = take_arguments()
    file_one = load_file(comparing_files_paths.get('first path'))
    file_two = load_file(comparing_files_paths.get('second path'))
    if comparing_files_paths.get('format') == 'plain':
        return render_and_gen_plain_diff(file_one, file_two)
    if comparing_files_paths.get('format') == 'json':
        return render_json(gen_nested_diff(file_one, file_two))

    return render_nested(gen_nested_diff(file_one, file_two))
