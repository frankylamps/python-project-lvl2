#!/usr/bin/env python3

from gendiff.gendiff import gendiff
from gendiff.formatters.render_json import render_json
from gendiff.formatters.render_nested import render_nested
from gendiff.formatters.render_plain import render_plain
from gendiff.parsers import load_file


def test_nested_json():  # noqa:D103
    file1 = load_file('gendiff/tests/fixtures/before.json')
    file2 = load_file('gendiff/tests/fixtures/after.json')
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    assert render_nested(gendiff(file1, file2)) == expected  # noqa:S101


def test_nested_yaml():  # noqa:D103
    file1 = load_file('gendiff/tests/fixtures/before.yaml')
    file2 = load_file('gendiff/tests/fixtures/after.yaml')
    expected = (open('gendiff/tests/fixtures/answer_nested.txt', 'r')).read()   # noqa: WPS515,E501
    assert render_nested(gendiff(file1, file2)) == expected  # noqa:S101


def test_plain_json():  # noqa:D103
    file1 = load_file('gendiff/tests/fixtures/before.json')
    file2 = load_file('gendiff/tests/fixtures/after.json')
    expected = (open('gendiff/tests/fixtures/answer_plain.txt', 'r')).read()   # noqa: WPS515,E501
    assert render_plain(gendiff(file1, file2)) == expected  # noqa:S101


def test_plain_yaml():  # noqa:D103
    file1 = load_file('gendiff/tests/fixtures/before.yaml')
    file2 = load_file('gendiff/tests/fixtures/after.yaml')
    expected = (open('gendiff/tests/fixtures/answer_plain.txt', 'r')).read()   # noqa: WPS515,E501
    assert render_plain(gendiff(file1, file2)) == expected  # noqa:S101


def test_json_json():  # noqa:D103
    file1 = load_file('gendiff/tests/fixtures/before.json')
    file2 = load_file('gendiff/tests/fixtures/after.json')
    expected = (open('gendiff/tests/fixtures/answer_json.json', 'r')).read()
    assert render_json(gendiff(file1, file2)) == expected  # noqa:S101


def test_json_yaml():  # noqa:D103
    file1 = load_file('gendiff/tests/fixtures/before.yaml')
    file2 = load_file('gendiff/tests/fixtures/after.yaml')
    expected = (open('gendiff/tests/fixtures/answer_json.json', 'r')).read()
    assert render_json(gendiff(file1, file2)) == expected  # noqa:S101
