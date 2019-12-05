from flask import request
from werkzeug.exceptions import BadRequest


def request_json(name, default=None, type=None, required: bool = False, error_message: str = None):
    value = request.json.get(name, default)
    if type is not None:
        return type(value)

    if required and not value:
        raise BadRequest(error_message if error_message else 'Required is {}'.format(name))

    return value
