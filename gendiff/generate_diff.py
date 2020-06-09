from gendiff.loader import load_file
from gendiff.gendiff import gendiff
from gendiff.cli import take_arguments
from gendiff.formatters.render_json import render_json
from gendiff.formatters.render_nested import render_nested
from gendiff.formatters.render_plain import render_plain


def generate_diff(path1, path2):
    file_one = load_file(path1)
    file_two = load_file(path2)
    difference = gendiff(file_one, file_two)
    return render_nested(difference)


def gendiff_main():
    comparing_files_paths = take_arguments()
    file_one = load_file(comparing_files_paths.get('first path'))
    file_two = load_file(comparing_files_paths.get('second path'))
    difference = gendiff(file_one, file_two)
    if comparing_files_paths['format'] == 'plain':
        print(render_plain(difference))
    if comparing_files_paths['format'] == 'json':
        print(render_json(difference))
    if comparing_files_paths['format'] == 'nested':
        print(render_nested(difference))
