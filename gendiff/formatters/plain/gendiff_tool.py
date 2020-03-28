def make_plain_structures(structure_old, structure_new):
    """Make plain structures out structures with nested items.

    Args:
        structure_old (dict): any dictionary
        structure_new (dict): any dictionary

    Returns:
        dict: dict with plain structures

    Example:
        structure_new: {'foo': {'bar': 1, 'baz': 2}}
        plain structure_new: {'foo.bar': 1, 'foo.baz': 2}
    """
    def make_plain_structure(structure):
        plain_structure = {}
        def add_paths(structure, previous_path=''):  # noqa:WPS442
            for path in structure.keys():
                if isinstance(structure[path], dict):
                    add_paths(structure[path], '{}.{}'.format(previous_path, path))
                else:
                    new_path = '{}.{}'.format(previous_path, path)[1:]
                    plain_structure[new_path] = structure[path]
        add_paths(structure)
        return plain_structure
    
    return {
        'plain_structure_old': make_plain_structure(structure_old),
        'plain_structure_new': make_plain_structure(structure_new)
    }
