#!/usr/bin/env python3

from gendiff.parsers import take_arguments
from gendiff.parsers import load_file
from gendiff.gendiff import gendiff
from gendiff.formatters.render_json import render_json
from gendiff.formatters.render_nested import render_nested
from gendiff.formatters.render_plain import render_plain


def main():
    comparing_files_paths = take_arguments()
    file_one = load_file(comparing_files_paths.get('first path'))
    file_two = load_file(comparing_files_paths.get('second path'))
    difference = gendiff(file_one, file_two)
    if comparing_files_paths.get('format') == 'plain':
        print(render_plain(difference))
    if comparing_files_paths.get('format') == 'json':
        print(render_json(difference))
    if not comparing_files_paths.get('format'):
        print(render_nested(difference))


if __name__ == '__main__':
    main()
