import json


def format(difference):
    json_dict = {}

    def format_inner(difference, previous_path=''):
        for key in difference.keys():
            status = difference[key][0]
            val = difference[key][1]
            if status == 'removed':
                json_dict['{}{}'.format(previous_path, key)] = 'Was removed'
            if status == 'added':
                if type(val) == dict:
                    val = 'complex value'
                json_dict['{}{}'.format(previous_path, key)] = "Was added with value: '{}'".format(val)  # noqa: E501
            if status == 'changed':
                json_dict['{}{}'.format(previous_path, key)] = "Was changed. From '{}' to '{}'".format(  # noqa: E501
                    val[0],
                    val[1]
                )
            if status == 'nested':
                format_inner(val, '{}{}.'.format(previous_path, key))
    format_inner(difference)
    return json.dumps(json_dict, sort_keys=True, indent=4)
