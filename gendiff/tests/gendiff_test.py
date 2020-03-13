#!/usr/bin/env python3

from gendiff.gendiff_func import return_gendiff
from gendiff.tests.fixtures.library import get_sorted_list
from gendiff.tests.fixtures.library import check_keywords_sequence

path1 = 'gendiff/tests/fixtures/d1.json'
path2 = 'gendiff/tests/fixtures/d2.json'

answer = '{\n  host: hexlet.io\n- proxy: 123.234.53.22\n+ verbose:' \
' True\n+ timeout: 20\n- timeout: 50\n}'  # noqa:E122


def test_one():
    a = get_sorted_list(answer)
    b = get_sorted_list(return_gendiff(path1, path2))
    assert a == b


def test_two():
    b = check_keywords_sequence(return_gendiff(path1, path2))
    assert b
