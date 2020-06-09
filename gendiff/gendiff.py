

def add_item(
    dictionary,
    new_key,
    value1,
    value2=None,
    sign=' ',
):
    """Add new item to the provided dictionary.

    Can get 2 values but only existing value will be added.

    Args:
        dictionary (dict): A dictionary where to add new item
        new_key (str): New key to add to the dictionary
        value1 (str): New value to add to the dictionary
        value2 (str): Old value to add to the dictionary
        sign (str, optional): A sign to add to the dict. Defaults to ' '.
    """
    new_value = value2
    if not value2:
        new_value = value1
    dictionary[new_key] = {
        sign: {
            'value': new_value,
        },
    }


def values_are_dicts(key, dict_old, dict_new):
    """Check if values of both dicts are also dicts.

    Args:
        key (str): A key for a value
        dict_old (dict): Old dictionary
        dict_new (dict): New dictionary

    Returns:
        [bool]: True or False
    """
    value1_is_dict = isinstance(dict_old.get(key), dict)
    value2_is_dict = isinstance(dict_new.get(key), dict)
    return value1_is_dict and value2_is_dict


def determine_sign(key, dict_old, dict_new):
    """Determine if the item was added deleted or exists in both dicts.

    Args:
        key (str): A key for the values
        dict_old (): Old dictionary with the value
        dict_new (): New dictionary with the value

    Returns:
        str: "+" , "-" or " "
    """
    intersected_keys = set(dict_old.keys()) & set(dict_new.keys())
    if key in intersected_keys:
        return ''
    if key in dict_new:
        return '+'
    return '-'


def gendiff(dict_old, dict_new):
    """Parse two dictionaries and make the dictionary with differencies.

    Args:
        dict_old (dict): Old dictionary
        dict_new (dict): New dictionary

    Returns:
        dict: dictionary with differencies which can be printed with parse func
    """
    diff = {}
    for key in set(dict_old.keys()) | set(dict_new.keys()):
        sign = determine_sign(key, dict_old, dict_new)
        value_new = dict_new.get(key)
        value_old = dict_old.get(key)
        if key in set(dict_old.keys()) & set(dict_new.keys()):
            if dict_old[key] == dict_new[key]:
                add_item(
                    diff,
                    key,
                    value_old,
                    value_new,
                )
            elif values_are_dicts(key, dict_old, dict_new):
                diff[key] = gendiff(
                    value_old,
                    value_new,
                )
            else:
                add_item(diff, key, value_new, sign='+')
                add_item(diff, key, value_old, sign='-')
                diff[key] = {
                    '-': {
                        'value': value_old,
                    },
                    '+': {
                        'value': value_new,
                    },
                }
        else:
            add_item(
                diff,
                key,
                value_old,
                value_new,
                sign=sign,
            )
    return diff
