#!/usr/bin/env python3

from gendiff.gendiff_main import gendiff
from gendiff.parsers.parsers import take_arguments


def test_json_nested(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.json'
    path2 = 'gendiff/tests/fixtures/file2_nested.json'
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    gendiff(take_arguments([path1, path2]))
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_json_flat(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_flat.json'
    path2 = 'gendiff/tests/fixtures/file2_flat.json'
    expected = (open('gendiff/tests/fixtures/answer_flat.txt', 'r')).read()   # noqa: WPS515,E501
    gendiff(take_arguments([path1, path2]))
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_nested(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.yaml'
    path2 = 'gendiff/tests/fixtures/file2_nested.yaml'
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    gendiff(take_arguments([path1, path2]))
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_flat(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_flat.yaml'
    path2 = 'gendiff/tests/fixtures/file2_flat.yaml'
    expected = (open('gendiff/tests/fixtures/answer_flat.txt', 'r')).read()   # noqa: WPS515,E501
    gendiff(take_arguments([path1, path2]))
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_yaml_nested_plain(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.yaml'
    path2 = 'gendiff/tests/fixtures/file2_nested.yaml'
    expected = (open('gendiff/tests/fixtures/answer_nested_plain.txt', 'r')).read()   # noqa: WPS515,E501
    gendiff(take_arguments(['-f', 'plain', path1, path2]))
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_json_nested_plain(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.json'
    path2 = 'gendiff/tests/fixtures/file2_nested.json'
    expected = (open('gendiff/tests/fixtures/answer_nested_plain.txt', 'r')).read()   # noqa: WPS515,E501
    gendiff(take_arguments(['-f', 'plain', path1, path2]))
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101


def test_json_nested_json(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1_nested.json'
    path2 = 'gendiff/tests/fixtures/file2_nested.json'
    expected = (open('gendiff/tests/fixtures/answer_nested_json.txt', 'r')).read()   # noqa: WPS515,E501
    gendiff(take_arguments(['-f', 'json', path1, path2]))
    my_print = capsys.readouterr()

    assert my_print.out == expected  # noqa:S101
