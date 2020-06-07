from gendiff.formatters.render_plain import get_attributes
from gendiff.formatters.render_plain import get_paths


def make_added_deleted_string(attributes, path):
    return '"{}": "Was changed. From \'{}\' to \'{}\'",'.format(
        path,
        attributes.get('-').get('value'),
        attributes.get('+').get('value'),
    )


def make_added_string(attributes, path):
    dict_value = attributes.get('+').get('value')
    if type(dict_value) == dict:
        return '"{}": "Was added with value: \'complex value\'",'.format(
            path,
        )
    return '"{}": "Was added with value: \'{}\'",'.format(
        path,
        dict_value,
    )


def render_json(diff):
    json_string = ''
    json_string += '{'
    all_paths = get_paths(diff)
    for path in all_paths:
        attributes = get_attributes(diff, path)
        keys = list(attributes.keys())
        if len(keys) > 1:
            json_string += make_added_deleted_string(attributes, path)
        elif keys[0] == '-':
            json_string += ('"{}": "Was removed",'.format(path))
        elif keys[0] == '+':
            json_string += make_added_string(attributes, path)
    json_string = json_string[: -1] + '}'
    return json_string
