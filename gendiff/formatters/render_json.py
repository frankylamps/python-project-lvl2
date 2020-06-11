from gendiff.formatters.render_plain import get_attributes
from gendiff.formatters.render_plain import get_paths


def render_json(diff):
    json_string = '{'
    all_paths = get_paths(diff)
    for path in all_paths:
        attributes = get_attributes(diff, path)
        keys = list(attributes.keys())
        if len(keys) > 1:
            json_string += '"{}": "Was changed. From \'{}\' to \'{}\'",'.format(  # noqa: E501
                path,
                attributes['-']['value'],
                attributes['+']['value'],
            )
        elif keys[0] == '-':
            json_string += ('"{}": "Was removed",'.format(path))
        elif keys[0] == '+':
            dict_value = attributes['+']['value']
            if type(dict_value) == dict:
                json_string += '"{}": "Was added with value: \'complex value\'",'.format(  # noqa: E501
                    path,
                )
            else:
                json_string += '"{}": "Was added with value: \'{}\'",'.format(
                    path,
                    dict_value,
                )
    json_string = json_string[: -1] + '}'
    return json_string
