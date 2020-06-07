
def get_attributes(gendiff_result, path):
    if type(path) == str:
        path = path.split('.')
    inner_dict = gendiff_result.get(path[0])
    if len(path) > 1:
        return get_attributes(inner_dict, path[1:])
    return inner_dict


def get_paths(diff, previous_path=None):
    path = []
    for key in diff.keys():
        inner_dict = diff[key]
        if {'-', ' ', '+'} & set(inner_dict.keys()):
            if previous_path:
                path.append('{}.{}'.format(previous_path, key))
            else:
                path.append(key)
        elif previous_path:
            path.extend(get_paths(inner_dict, previous_path))
        else:
            path.extend(get_paths(inner_dict, key))
    path.sort()
    return path


def make_added_string(attributes, path):
    dict_value = attributes.get('+').get('value')
    if type(dict_value) == dict:
        return "Property '{}' was added with value: 'complex value'\n".format(
            path,
        )
    return "Property '{}' was added with value: '{}'\n".format(
        path,
        dict_value,
    )


def make_added_deleted_string(attributes, path):
    return "Property '{}' was changed. From '{}' to '{}'\n".format(
        path,
        attributes.get('-').get('value'),
        attributes.get('+').get('value'),
    )


def render_plain(diff):
    str_to_render = ''
    all_paths = get_paths(diff)
    for path in all_paths:
        attributes = get_attributes(diff, path)
        keys = list(attributes.keys())
        if len(keys) > 1:
            str_to_render += make_added_deleted_string(attributes, path)
        elif keys[0] == '-':
            str_to_render += ("Property '{}' was removed\n".format(path))
        elif keys[0] == '+':
            str_to_render += make_added_string(attributes, path)
    return str_to_render[:-1]
