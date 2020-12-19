def make_dict_string(attributes, indention):
    """Convert python dict to string can be pretty printed.

    Args:
        attributes (dict): python dict
        indention (int): indention

    Returns:
        str: can be pretty printed with print function
    """
    dict_structure = ''
    for key in attributes.keys():
        if type(attributes[key]) == dict:
            dict_structure += ('{}{}: {{\n'.format(' ' * indention, key))
            dict_structure += make_dict_string(
                attributes[key],
                indention + 4,
            )
            dict_structure += ('{}}}\n'.format(' ' * indention))
        else:
            dict_structure += ('{}{}: {}\n'.format(
                ' ' * indention,
                key,
                attributes[key],
            ))
    return dict_structure


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
    string_to_print = ""
    if type(end_value) == dict:
        string_to_print += ('{}{} {}: {{\n'.format(
            ' ' * indention,
            sign,
            part_of_path,
        ))
        string_to_print += make_dict_string(end_value, indention + 6)
        string_to_print += ('{}}}\n'.format(' ' * (indention + 2)))
    else:
        string_to_print += '{}{} {}: {}\n'.format(
            ' ' * indention,
            sign,
            part_of_path,
            end_value,
        )
    return string_to_print


def format(difference, indention=2, original=True):
    str_to_print = ''
    if original:
        str_to_print += '{\n'
    for key in sorted(difference.keys()):
        status = difference[key][0]
        val = difference[key][1]
        if status == 'added':
            str_to_print += make_substring(val, key, '+', indention)
        if status == 'removed':
            str_to_print += make_substring(val, key, '-', indention)
        if status == 'unchanged':
            str_to_print += make_substring(val, key, ' ', indention)
        if status == 'changed':
            str_to_print += make_substring(val[0], key, '-', indention)
            str_to_print += make_substring(val[1], key, '+', indention)
        if status == 'nested':
            str_to_print += '  {}{}: {{\n'.format(' ' * indention, key)
            str_to_print += format(val, indention + 4, False)
            str_to_print += '{}  }}\n'.format(' ' * indention)
    if original:
        str_to_print += '}'
    return str_to_print
