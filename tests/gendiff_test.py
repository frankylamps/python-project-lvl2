from gendiff.gendiff import gendiff
from gendiff.formatters.render_json import render_json
from gendiff.formatters.render_nested import render_nested
from gendiff.formatters.render_plain import render_plain
from gendiff.loader import load_file


def test_nested_json():
    file1 = load_file('tests/fixtures/before.json')
    file2 = load_file('tests/fixtures/after.json')
    expected = (open('tests/fixtures/answer_nested.txt', 'r')).read()
    assert render_nested(gendiff(file1, file2)) == expected


def test_nested_yaml():
    file1 = load_file('tests/fixtures/before.yaml')
    file2 = load_file('tests/fixtures/after.yaml')
    expected = (open('tests/fixtures/answer_nested.txt', 'r')).read()
    assert render_nested(gendiff(file1, file2)) == expected


def test_plain_json():
    file1 = load_file('tests/fixtures/before.json')
    file2 = load_file('tests/fixtures/after.json')
    expected = (open('tests/fixtures/answer_plain.txt', 'r')).read()
    assert render_plain(gendiff(file1, file2)) == expected


def test_plain_yaml():
    file1 = load_file('tests/fixtures/before.yaml')
    file2 = load_file('tests/fixtures/after.yaml')
    expected = (open('tests/fixtures/answer_plain.txt', 'r')).read()
    assert render_plain(gendiff(file1, file2)) == expected


def test_json_json():
    file1 = load_file('tests/fixtures/before.json')
    file2 = load_file('tests/fixtures/after.json')
    expected = (open('tests/fixtures/answer_json.json', 'r')).read()
    assert render_json(gendiff(file1, file2)) == expected


def test_json_yaml():
    file1 = load_file('tests/fixtures/before.yaml')
    file2 = load_file('tests/fixtures/after.yaml')
    expected = (open('tests/fixtures/answer_json.json', 'r')).read()
    assert render_json(gendiff(file1, file2)) == expected
