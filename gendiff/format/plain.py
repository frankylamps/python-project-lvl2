
def format(difference, previous_path=''):
    path = ""
    for key in sorted(difference.keys()):
        status = difference[key][0]
        val = difference[key][1]
        if status == 'removed':
            path += "Property '{}{}' was removed\n".format(previous_path, key)
        if status == 'added':
            if type(val) == dict:
                val = 'complex value'
            path += "Property '{}{}' was added with value: '{}'\n".format(previous_path, key, val)  # noqa: E501
        if status == 'changed':
            path += "Property '{}{}' was changed. From '{}' to '{}'\n".format(
                previous_path,
                key,
                val[0],
                val[1]
            )
        if status == 'nested':
            path += format(val, '{}{}.'.format(previous_path, key))
    if previous_path:
        return path
    return path[:-1]
