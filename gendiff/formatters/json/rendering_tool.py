import json


def make_dict(nested_diff, render_dict=None):
    """Convert nested gendiff result to json-compatibe dict.

    Args:
        nested_diff (dict): gendiff dict to be converted
        render_dict (dict, optional): technical arg, do not use!

    Returns:
        arg: json-compatible dictionary
    """
    if not render_dict:
        render_dict = {}
    indexes = list(nested_diff.keys())
    indexes.sort()
    for index in indexes:
        a = nested_diff[index]
        if isinstance(a.get('value'), dict):
            if a.get('type') == 'changed':
                render_dict[(a.get('key'))] = make_dict(a.get('value'))
            else:
                render_dict['{} {}'.format(
                    a.get('sign'),
                    a.get('key'),
                )] = a.get('value')
        else:
            render_dict['{} {}'.format(
                a.get('sign'),
                a.get('key'),
            )] = a.get('value')
    return render_dict


def render_json(nested_diff):
    """Print out python dict in json-style.

    Args:
        nested_diff (dict): result of original gendiff function
    """
    new_r = make_dict(nested_diff)
    print(json.dumps(new_r, indent=4))
