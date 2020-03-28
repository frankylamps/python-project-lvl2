
def add_item(  # noqa:WPS211
    dictionary,
    new_key,
    value_new,
    value_old=None,
    sign=' ',
    item_type='',
):
    """Add new item to the provided dictionary.

    Can get 2 values but only existing value will be added.

    Args:
        dictionary (dict): A dictionary where to add new item
        new_key (str): New key to add to the dictionary
        value_new (str): New value to add to the dictionary
        value_old (str): Old value to add to the dictionary
        sign (str, optional): A sign to add to the dict. Defaults to ' '.
        item_type (str, optional): A sign to add to the dict. Defaults to ''.
    """
    if dictionary:
        index = max(list(dictionary.keys())) + 1
    else:
        index = 1
    new_value = value_old
    if not value_old:
        new_value = value_new
    dictionary[index] = {
        'key': new_key,
        'value': new_value,
        'sign': sign,
        'type': item_type,
    }


def get_all_keys(dict_old, dict_new):
    """Return all keys from 2 dictionaries in alphabetical order.

    Args:
        dict_old (dict): Old doctionary
        dict_new (dict): New dictionary

    Returns:
        [list]: list of all keys
    """
    all_keys_set = set(dict_old.keys()) | set(dict_new.keys())
    all_keys_list = list(all_keys_set)
    all_keys_list.sort()
    return all_keys_list


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


def determine_dict_type(key, dict_old, dict_new):
    """Find out if values are dictionaries and whether have been changed.

    Args:
        key (str): A key for the values
        dict_old (): Old dictionary with the value
        dict_new (): New dictionary with the value

    Returns:
        str: "unchanged", "changed" or "" if both values are not dicts
    """
    if values_are_dicts(key, dict_old, dict_new):
        if dict_old.get(key) == dict_new.get(key):
            return 'unchanged'
        return 'changed'
    return ''


def gen_nested_diff(dict_old, dict_new):  # noqa:WPS210
    """Parse two dictionaries and make the dictionary with differencies.

    Args:
        dict_old (dict): Old dictionary
        dict_new (dict): New dictionary

    Returns:
        dict: dictionary with differencies which can be printed with parse func
    """
    diff = {}
    for key in get_all_keys(dict_old, dict_new):
        sign = determine_sign(key, dict_old, dict_new)
        item_type = determine_dict_type(key, dict_old, dict_new)
        value_new = dict_new.get(key)
        value_old = dict_old.get(key)
        if key in set(dict_old.keys()) & set(dict_new.keys()):
            if dict_old[key] == dict_new[key]:
                add_item(
                    diff,
                    key,
                    value_old,
                    value_new,
                    item_type=item_type,
                )
            elif values_are_dicts(key, dict_old, dict_new):
                add_item(
                    diff,
                    key,
                    gen_nested_diff(
                        value_old,
                        value_new,
                    ),
                    item_type=item_type,
                )
            else:
                add_item(diff, key, value_new, sign='+')
                add_item(diff, key, value_old, sign='-')
        else:
            add_item(
                diff,
                key,
                value_old,
                value_new,
                sign=sign,
                item_type=item_type,
            )
    return diff
