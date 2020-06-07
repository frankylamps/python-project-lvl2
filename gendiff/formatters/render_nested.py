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


def render_nested(difference, indention=2, original=True):
    """Convert result of gendiff func into string which can be pretty printed.

    Args:
        difference (dict): result of gendiff func
        indention (int, optional): Defaults to 2.
        original (bool, optional): False in recursion. Defaults to True.

    Returns:
        str: string that can be pretty printed as nested structure
    """
    str_to_print = ''
    if original:
        str_to_print += '{\n'

    parts_of_path = list(difference.keys())
    parts_of_path.sort()
    for part_of_path in parts_of_path:
        if set(difference[part_of_path].keys()) & {'+', '-', ' '}:
            for sign in difference[part_of_path].keys():
                str_to_print += make_substring(
                    difference[part_of_path][sign]['value'],
                    part_of_path,
                    sign,
                    indention,
                )
        else:
            str_to_print += '  {}{}: {{\n'.format(  # noqa:P101
                ' ' * indention,
                part_of_path,
            )
            str_to_print += render_nested(
                difference[part_of_path],
                indention + 4,
                original=False,
            )
            str_to_print += '{}  }}\n'.format(' ' * indention)
    if original:
        str_to_print += '}'
    return str_to_print
