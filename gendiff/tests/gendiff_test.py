#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.tools.gendiff_tool import gen_diff
from gendiff.parsers.parsers import make_json_files
from gendiff.parsers.parsers import make_yaml_files
from gendiff.tools.rendering_tool import render


def test_json_nested(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.json'
    path2 = 'gendiff/tests/fixtures/file2_nested.json'
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    engine(gen_diff, make_json_files([path1, path2]), render)
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_json_flat(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_flat.json'
    path2 = 'gendiff/tests/fixtures/file2_flat.json'
    expected = (open('gendiff/tests/fixtures/answer_flat.txt', 'r')).read()   # noqa: WPS515,E501
    engine(gen_diff, make_json_files([path1, path2]), render)
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_nested(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.yaml'
    path2 = 'gendiff/tests/fixtures/file2_nested.yaml'
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    engine(gen_diff, make_yaml_files([path1, path2]), render)
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_flat(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_flat.yaml'
    path2 = 'gendiff/tests/fixtures/file2_flat.yaml'
    expected = (open('gendiff/tests/fixtures/answer_flat.txt', 'r')).read()   # noqa: WPS515,E501
    engine(gen_diff, make_yaml_files([path1, path2]), render)
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101
