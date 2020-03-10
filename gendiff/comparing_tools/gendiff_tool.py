def add_item(result, key, value, sign=' '):
    if result:
        return '{}\n{} {}: {}'.format(result, sign, key, value)
    return '{} {}: {}'.format(sign, key, value)


def arrange_result(comparison):
    return '{{\n{}\n}}'.format(comparison)


def generate_diff(d1, d2):
    intersected_keys = set(d1.keys()) & set(d2.keys())
    all_keys = set(d1.keys()) | set(d2.keys())
    comparison = ''
    for key in all_keys:
        if key in intersected_keys:
            if d1[key] == d2[key]:
                comparison = add_item(comparison, key, d1[key])
            else:
                comparison = add_item(comparison, key, d2[key], '+')
                comparison = add_item(comparison, key, d1[key], '-')

        elif key in set(d1.keys()):
            comparison = add_item(comparison, key, d1[key], '-')
        else:
            comparison = add_item(comparison, key, d2[key], '+')
    return arrange_result(comparison)





