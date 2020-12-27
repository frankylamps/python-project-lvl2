from gendiff.format.json import format as json  # noqa: F401
from gendiff.format.plain import format as plain  # noqa: F401
from gendiff.format.default import format as default  # noqa: F401
import argparse


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default',
)


def formatter(name):
    if name == JSON:
        return json
    elif name == PLAIN:
        return plain
    elif name == DEFAULT:
        return default
    raise argparse.ArgumentTypeError(
        'Unknown formatter: {}'.format(name)
    )
