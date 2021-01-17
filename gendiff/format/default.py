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


symbols = {
    'added': '+',
    'removed': '-',
    'unchanged': ' ',
}


def format(difference, indention=2, original=True):
    list_of_strings = []
    for k, v in sorted(difference.items()):
        status = v[0]
        val = v[1]
        if status == 'changed':
            list_of_strings.extend(make_substring(val[0], k, symbols['removed'], indention))
            list_of_strings.extend(make_substring(val[1], k, symbols['added'], indention))
        if status == 'nested':
            list_of_strings.append('  {}{}: {{'.format(' ' * indention, k))
            list_of_strings.extend(format(val, indention + 4, False))
            list_of_strings.append('{}  }}'.format(' ' * indention))
        elif status in symbols.keys():
            list_of_strings.extend(make_substring(val, k, symbols[status], indention))
    if original:
        list_of_strings.insert(0, '{')
        list_of_strings.append('}')
        return "\n".join(list_of_strings)
    return list_of_strings
