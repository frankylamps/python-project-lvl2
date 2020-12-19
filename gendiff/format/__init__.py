from gendiff.format.json import format as json  # noqa: F401
from gendiff.format.plain import format as plain  # noqa: F401
from gendiff.format.default import format as default  # noqa: F401


FORMATTERS = (JSON, PLAIN, DEFAULT) = (
    'json', 'plain', 'default'
)
