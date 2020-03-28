def get_all_keys(structure_old, structure_new):
    """Return all keys from 2 dictionaries in alphabetical order.

    Args:
        structure_old (dict): Old doctionary
        structure_new (dict): New structure

    Returns:
        [list]: list of all keys
    """
    all_keys_set = set(structure_old.keys()) | set(structure_new.keys())
    all_keys_list = list(all_keys_set)
    all_keys_list.sort()
    return all_keys_list


def get_unique_path(path, paths):
    """Get the unique part of the path amoung all paths.

    Args:
        path (str): e.g. foo.bar.baz
        paths (list): e.g. ['foo', 'aggs']

    Returns:
        str: e.g. "foo.bar"
    """
    splitted_path = path.split('.')
    path_length = len(splitted_path)
    counter = 1
    while counter <= path_length:
        found = False
        for new_path in paths:
            if '.'.join(splitted_path[: counter]) in new_path:
                if new_path.index('.'.join(splitted_path[: counter])) == 0:
                    found = True
        if not found:
            return '.'.join(splitted_path[: counter])
        counter += 1


def render_plain(dict_with_two_structures):
    """Print out the difference between two structures in plain style.

    Args:
        structure_old (dict): Old structure
        structure_new (dict): New structure
    """
    structure_old = dict_with_two_structures.get('plain_structure_old')
    structure_new = dict_with_two_structures.get('plain_structure_new')

    for path in get_all_keys(structure_old, structure_new):
        if structure_old.get(path) == structure_new.get(path):
            continue
        elif path in set(structure_old.keys()) & set(structure_new.keys()):
            print("Property '{}' was changed. From '{}' to '{}'".format(
                path,
                structure_old[path],
                structure_new[path]
            ))
        elif path in structure_old.keys():
            unique_path = get_unique_path(path, list(structure_new.keys()))
            print("Property '{}' was removed".format(unique_path))
        elif path in structure_new.keys():
            unique_path = get_unique_path(path, list(structure_old.keys()))
            if len(unique_path) < len(path):
                new_value = 'complex value'
            else:
                new_value = structure_new[path]
            print("Property '{}' was added with value: '{}'".format(
                unique_path,
                new_value,
            ))
