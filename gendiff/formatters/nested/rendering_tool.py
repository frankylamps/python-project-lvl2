

def print_dict_as_value(dictionary, indention):
    """Print structure with all items in the dictionary.

    Arguments:
        dictionary: {dict} A dictionary with items to be printed
        indention: {int} An indention for the printed structure
    """
    for key, value in dictionary.items():  # noqa:WPS110
        if type(value) == dict:  # noqa:WPS516
            print('{}{}: {}'. format(' ' * (indention + 6), key, '{'))  # noqa:P101,E501
            print_dict_as_value(value, indention + 4)
            print('{}{}'. format(' ' * (indention + 6), '}'))  # noqa:P101
        else:
            print('{}{}: {}'. format(  # noqa:P101
                ' ' * (indention + 6),
                key,
                value,
            ))


def print_dict_structure(attributes, indention):
    """Print structure of flat and nested dictionaries.

    Arguments:
        attributes: {dict} A dictionary with signs, keys, values
        indention: {int} An indention for the printed structure
    """
    print('{}{} {}: {}'.format(  # noqa:P101
        ' ' * indention,
        attributes.get('sign'),
        attributes.get('key'),
        '{',
    ))
    simple_dict = attributes.get('value')
    print_dict_as_value(simple_dict, indention)
    print('{}{}'.format(' ' * (indention + 2), '}'))  # noqa:P101


def render_nested(difference, indention=2, original=True):
    """Render the output of the gen_diff function.

    Arguments:
        difference: {dict} Result of gen_diff function
        indention: {int} An indention for the printed structure
    """
    if original:
        print('{')
    indexes = list(difference.keys())
    indexes.sort()
    for index in indexes:
        attributes = difference[index]
        if isinstance(attributes.get('value'), dict):
            if attributes.get('type') == 'changed':
                print('  {}{}: {}'.format(  # noqa:P101
                    ' ' * indention,
                    attributes.get('key'),
                    '{',
                ))
                render_nested(attributes.get('value'), indention + 4, original=False)  # noqa:E501
                print('{}{}'.format(' ' * (indention + 2), '}'))  # noqa:P101
            else:
                print_dict_structure(attributes, indention)
        else:
            print('{}{} {}: {}'.format(  # noqa:P101
                ' ' * indention,
                attributes.get('sign'),
                attributes.get('key'),
                attributes.get('value'),
            ))
    if original:
        print('}')
