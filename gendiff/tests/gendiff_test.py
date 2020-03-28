#!/usr/bin/env python3

from gendiff.engine import engine
from gendiff.parsers.parsers import take_arguments
from gendiff.formatters.plain.gendiff_tool import make_plain_structures
from gendiff.formatters.nested.gendiff_tool import gen_nested_diff
from gendiff.formatters.plain.rendering_tool import render_plain
from gendiff.formatters.nested.rendering_tool import render_nested


def test_json_nested(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.json'
    path2 = 'gendiff/tests/fixtures/file2_nested.json'
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    engine(
        gen_nested_diff,
        take_arguments([path1, path2]),
        render_nested,
        make_plain_structures,
        render_plain,
    )
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_json_flat(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_flat.json'
    path2 = 'gendiff/tests/fixtures/file2_flat.json'
    expected = (open('gendiff/tests/fixtures/answer_flat.txt', 'r')).read()   # noqa: WPS515,E501
    engine(
        gen_nested_diff,
        take_arguments([path1, path2]),
        render_nested,
        make_plain_structures,
        render_plain,
    )
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_nested(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.yaml'
    path2 = 'gendiff/tests/fixtures/file2_nested.yaml'
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    engine(
        gen_nested_diff,
        take_arguments([path1, path2]),
        render_nested,
        make_plain_structures,
        render_plain,
    )
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_flat(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_flat.yaml'
    path2 = 'gendiff/tests/fixtures/file2_flat.yaml'
    expected = (open('gendiff/tests/fixtures/answer_flat.txt', 'r')).read()   # noqa: WPS515,E501
    engine(
        gen_nested_diff,
        take_arguments([path1, path2]),
        render_nested,
        make_plain_structures,
        render_plain,
    )
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_nested_plain(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.yaml'
    path2 = 'gendiff/tests/fixtures/file2_nested.yaml'
    expected = (open('gendiff/tests/fixtures/answer_nested_plain.txt', 'r')).read()   # noqa: WPS515,E501
    engine(
        gen_nested_diff,
        take_arguments(['-f', 'plain', path1, path2]),
        render_nested,
        make_plain_structures,
        render_plain,
    )
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_json_nested_plain(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.json'
    path2 = 'gendiff/tests/fixtures/file2_nested.json'
    expected = (open('gendiff/tests/fixtures/answer_nested_plain.txt', 'r')).read()   # noqa: WPS515,E501
    engine(
        gen_nested_diff,
        take_arguments(['-f', 'plain', path1, path2]),
        render_nested,
        make_plain_structures,
        render_plain,
    )
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101
