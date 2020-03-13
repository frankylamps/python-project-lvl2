def find_second_index(value, items):  # noqa:WPS110
    """Find the 2-nd index of the value in the items."""  # noqa:DAR101, DAR201
    def find_index(value, items):  # noqa:WPS442, WPS110
        for index, item in enumerate(items):  # noqa:WPS110
            if item == value:
                return index

    cursor = iter(items)
    index1 = find_index(value, cursor)
    index2 = find_index(value, cursor)
    if index2 is not None:
        return index1 + index2 + 1
    return None


def get_keys(json_like_string):
    """Get all keys from json-like string."""  # noqa:DAR101, DAR201
    def erase_after_colon(string):
        return string[:string.find(':')]

    string1 = json_like_string.split('\n')
    string2 = list(filter(lambda x: len(x) > 1, string1))  # noqa:WPS111
    string3 = list(map(lambda x: x[2:], string2))  # noqa:WPS111
    return list(map(erase_after_colon, string3))


def check_keywords_sequence(json_like_string):
    """Find out if all duplicate values are placed together."""  # noqa:DAR101, DAR201
    keys = get_keys(json_like_string)
    for (n, i) in enumerate(keys):  # noqa:WPS111
        next_index = find_second_index(i, keys)
        if next_index and next_index > n + 1:
            return False
        return True


s1 = '{\n  host: hexlet.io\n+ timeout: 20\n- timeout: 50\n- proxy:' \
    '123.234.53.22\n+ verbose: True\n}'

s2 = '- timeout: 50\n- proxy:' \
    '123.234.53.22\n+ verbose: True\n{\n  host: hexlet.io\n+ timeout: 20\n}'

# print(get_keys(s1))
# print(check_keywords_sequence(s1))


def get_sorted_list(json_like_string):
    string_as_list = json_like_string.split('\n')
    string_as_list.sort()
    return string_as_list

# print(get_sorted_list(s1))