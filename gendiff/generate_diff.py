import yaml
import json
import os


def load_file(path):
    if os.path.splitext(path)[1] == '.yaml':
        return yaml.load((open(path, 'r')), Loader=yaml.SafeLoader)
    if os.path.splitext(path)[1] == '.json':
        return json.load(open(path))


def gendiff_inner(dict_old, dict_new):
    diff = {}
    added_values = set(dict_new.keys()) - set(dict_old.keys())
    removed_values = set(dict_old.keys()) - set(dict_new.keys())
    for key in set(dict_old.keys()) | set(dict_new.keys()):
        value_old, value_new = dict_old.get(key), dict_new.get(key)
        if value_old and value_new:
            if value_old == value_new:
                diff[key] = ('unchanged', value_old)
            elif isinstance(value_old, dict) and isinstance(value_new, dict):
                diff[key] = ('nested', gendiff_inner(value_old, value_new))
            elif value_old != value_new:
                diff[key] = ('changed', (dict_old.get(key), dict_new.get(key)))
        elif key in removed_values:
            diff[key] = ('removed', dict_old[key])
        elif key in added_values:
            diff[key] = ('added', dict_new[key])
    return diff


def gendiff_main(path_to_file1, path_to_file2, output_format):
    file_one = load_file(path_to_file1)
    file_two = load_file(path_to_file2)
    difference = gendiff_inner(file_one, file_two)
    return output_format(difference)
