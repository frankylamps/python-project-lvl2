import json
import pytest
from gendiff.generate_diff import gendiff_main
from gendiff import format


path_json_f1 = 'tests/fixtures/before.json'
path_json_f2 = 'tests/fixtures/after.json'
path_yaml_f1 = 'tests/fixtures/before.yaml'
path_yaml_f2 = 'tests/fixtures/after.yaml'
expected_nested = 'tests/fixtures/answer_nested.txt'
expected_plain = 'tests/fixtures/answer_plain.txt'
expected_json = 'tests/fixtures/answer_json.json'


@pytest.mark.parametrize('path_f1, path_f2, f, expected', [
    (path_json_f1, path_json_f2, format.default, expected_nested),
    (path_yaml_f1, path_yaml_f2, format.default, expected_nested),
    (path_json_f1, path_json_f2, format.plain, expected_plain),
    (path_yaml_f1, path_yaml_f2, format.plain, expected_plain),
])
def test_nested_plain(path_f1, path_f2, f, expected):
    assert gendiff_main(path_f1, path_f2, f) == open(expected, 'r').read()


@pytest.mark.parametrize('path_f1, path_f2, f', [
    (path_json_f1, path_json_f2, format.json),
    (path_json_f1, path_json_f2, format.json), 
])
def test_json(path_f1, path_f2, f):
    assert json.loads(gendiff_main(path_f1, path_f2, f)) == json.load(open(expected_json, 'r'))
