#!/usr/bin/env python3

from gendiff.tests.fixtures.library import get_sorted_list
from gendiff.tests.fixtures.library import check_keywords_sequence
from gendiff.engine import engine
from gendiff.tools.gendiff_tools import generate_diff
from gendiff.parsers.parsers import make_json_files
from gendiff.parsers.parsers import make_yaml_files


def test_json_one(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    answer = (open('gendiff/tests/fixtures/answer1.txt', 'r')).read()   # noqa: WPS515,E501
    expected = get_sorted_list(answer)

    my_answer = get_sorted_list(
        engine(generate_diff, make_json_files([path1, path2])),
    )
    assert my_answer == expected  # noqa:S101


def test_json_two():
    """Check if the same values are placed together."""  # noqa:DAR101, DAR201
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    if_correct = check_keywords_sequence(
        engine(generate_diff, make_json_files([path1, path2])),
    )
    assert if_correct  # noqa:S101


def test_yaml_one(capsys):  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1.yaml'
    path2 = 'gendiff/tests/fixtures/file2.yaml'
    answer = (open('gendiff/tests/fixtures/answer1.txt', 'r')).read()   # noqa: WPS515,E501
    expected = get_sorted_list(answer)

    my_answer = get_sorted_list(
        engine(generate_diff, make_yaml_files([path1, path2])),
    )
    assert my_answer == expected  # noqa:S101


def test_yaml_two():
    """Check if the same values are placed together."""  # noqa:DAR101, DAR201
    path1 = 'gendiff/tests/fixtures/file1.yaml'
    path2 = 'gendiff/tests/fixtures/file2.yaml'
    if_correct = check_keywords_sequence(
        engine(generate_diff, make_yaml_files([path1, path2])),
    )
    assert if_correct  # noqa:S101