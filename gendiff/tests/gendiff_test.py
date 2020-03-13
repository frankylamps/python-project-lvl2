#!/usr/bin/env python3

from gendiff.gendiff_func import return_gendiff
from gendiff.tests.fixtures.library import get_sorted_list
from gendiff.tests.fixtures.library import check_keywords_sequence


def test_one():  # noqa:D103
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    answer = (open('gendiff/tests/fixtures/answer1.txt', 'r')).read()   # noqa: WPS515,E501
    correct_answer = get_sorted_list(answer)
    my_answer = get_sorted_list(return_gendiff(path1, path2))
    assert my_answer == correct_answer  # noqa:S101


def test_two():
    """Check if the same values are placed together."""  # noqa:DAR101, DAR201
    path1 = 'gendiff/tests/fixtures/file1.json'
    path2 = 'gendiff/tests/fixtures/file2.json'
    if_correct = check_keywords_sequence(return_gendiff(path1, path2))
    assert if_correct
