from gendiff.formatters.nested.gendiff_tool import get_all_keys


def make_plain_structure(structure):
    """Make plain structures out of structures with nested items.

    Args:
        structure (dict): any dictionary

    Returns:
        dict: dict with plain structures

    Example:
        structure_new: {'foo': {'bar': 1, 'baz': 2}}
        plain structure_new: {'foo.bar': 1, 'foo.baz': 2}
    """
    plain_structure = {}

    def add_paths(structure, previous_path=''):  # noqa:WPS442
        for path in structure.keys():
            if isinstance(structure[path], dict):
                add_paths(
                    structure[path],
                    '{}.{}'.format(previous_path, path),
                )
            else:
                new_path = '{}.{}'.format(previous_path, path)[1:]
                plain_structure[new_path] = structure[path]
    add_paths(structure)
    return plain_structure  # noqa:WPS331


def get_unique_path(path, paths):
    """Get the unique part of the path amoung all paths.

    Args:
        path (str): e.g. 'foo.bar.baz.foo'
        paths (list): e.g. ['foo', 'bar.eggz']

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


def render_and_gen_plain_diff(structure_old, structure_new):  # noqa:WPS231
    """Print out the difference between two structures in plain style.

    Args:
        structure_old (dict): Old structure
        structure_new (dict): New structure
    """
    structure_old = make_plain_structure(structure_old)
    structure_new = make_plain_structure(structure_new)

    for path in get_all_keys(structure_old, structure_new):
        if structure_old.get(path) == structure_new.get(path):
            continue
        elif path in set(structure_old.keys()) & set(structure_new.keys()):
            print("Property '{}' was changed. From '{}' to '{}'".format(
                path,
                structure_old[path],
                structure_new[path],
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
