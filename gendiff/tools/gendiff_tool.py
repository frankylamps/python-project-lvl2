def add_item(string, key, value, sign=' '):  # noqa: WPS110
    """Return a string with added key and value."""  # noqa: DAR101, DAR201
    if string:
        return '{}\n{} {}: {}'.format(string, sign, key, value)  # noqa: P101
    return '{} {}: {}'.format(sign, key, value)  # noqa: P101


def arrange_result(string):
    """Return a string in curly brackets."""  # noqa: DAR101, DAR201
    return '{{\n{}\n}}'.format(string)  # noqa: P101


def generate_diff(d1, d2):
    """Return a string with differences between two dictionaries.

    "+" if it's a new key or new value

    "-" if key or value has been deleted or changed in d2

    " " if the key or value haven't been changed

    Args:
        d1: (dict) old dictionary
        d2: (dict) new dictionary

    Returns:
        string: (str) json-like string with comparison result

    """
    intersected_keys = set(d1.keys()) & set(d2.keys())
    all_keys = set(d1.keys()) | set(d2.keys())
    comparison = ''
    for key in all_keys:
        if key in intersected_keys:
            if d1[key] == d2[key]:
                comparison = add_item(comparison, key, d1[key])
            else:
                comparison = add_item(comparison, key, d2[key], '+')
                comparison = add_item(comparison, key, d1[key], '-')

        elif key in set(d1.keys()):
            comparison = add_item(comparison, key, d1[key], '-')
        else:
            comparison = add_item(comparison, key, d2[key], '+')
    return arrange_result(comparison)
