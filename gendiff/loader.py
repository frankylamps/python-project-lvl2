import yaml
import json


def load_file(path):
    """Load json or yaml file and convert it to python dict.

    Args:
        path (str): path to file

    Returns:
        dict:
    """
    if path[path.rfind('.') + 1:] == 'yaml':
        return yaml.load((open(path, 'r')), Loader=yaml.SafeLoader)
    if path[path.rfind('.') + 1:] == 'json':
        return json.load(open(path))
