def make_dict_string(attributes, indention):
    list_of_strings = []
    for key in attributes.keys():
        if type(attributes[key]) == dict:
            list_of_strings.append('{}{}: {{'.format(' ' * indention, key))
            list_of_strings.extend(make_dict_string(
                attributes[key],
                indention + 4,
            ))
            list_of_strings.append('{}}}'.format(' ' * indention))
        else:
            list_of_strings.append('{}{}: {}'.format(
                ' ' * indention,
                key,
                attributes[key],
            ))
    return list_of_strings


def make_substring(end_value, part_of_path, sign, indention):
    """Create substring out of end value.

    Args:
        end_value (dict, str, int): end value from gendiff result
        part_of_path (str): just part of path
        sign (str): "+", "-", " ".
        indention (int): just indention

    Returns:
        str: string which can be pretty printed
    """
    list_of_strings = []
    if type(end_value) == dict:
        list_of_strings.append('{}{} {}: {{'.format(
            ' ' * indention,
            sign,
            part_of_path,
        ))
        list_of_strings.extend(make_dict_string(end_value, indention + 6))
        list_of_strings.append('{}}}'.format(' ' * (indention + 2)))
    else:
        list_of_strings.append('{}{} {}: {}'.format(
            ' ' * indention,
            sign,
            part_of_path,
            end_value,
        ))
    return list_of_strings


def format(difference, indention=2, original=True):
    list_of_strings = []
    if original:
        list_of_strings.append('{')
    for key in sorted(difference.keys()):
        status = difference[key][0]
        val = difference[key][1]
        if status == 'added':
            list_of_strings.extend(make_substring(val, key, '+', indention))
        if status == 'removed':
            list_of_strings.extend(make_substring(val, key, '-', indention))
        if status == 'unchanged':
            list_of_strings.extend(make_substring(val, key, ' ', indention))
        if status == 'changed':
            list_of_strings.extend(make_substring(val[0], key, '-', indention))
            list_of_strings.extend(make_substring(val[1], key, '+', indention))
        if status == 'nested':
            list_of_strings.append('  {}{}: {{'.format(' ' * indention, key))
            list_of_strings.extend(format(val, indention + 4, False))
            list_of_strings.append('{}  }}'.format(' ' * indention))
    if original:
        list_of_strings.append('}')
        return "\n".join(list_of_strings)
    return list_of_strings
