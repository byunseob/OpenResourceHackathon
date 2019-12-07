from dataclasses import is_dataclass, asdict
from datetime import datetime, date, time
from decimal import Decimal

from flask import request
from werkzeug.exceptions import BadRequest


def request_param(name, default=None, type=None, required: bool = False, error_message: str = None):
    value = request.values.get(name, default=default, type=type)

    if required and not value:
        raise BadRequest(error_message if error_message else 'Required is {}'.format(name))

    return value


def request_json(name, default=None, type=None, required: bool = False, error_message: str = None):
    value = request.json.get(name, default)
    if type is not None:
        return type(value)

    if required and not value:
        raise BadRequest(error_message if error_message else 'Required is {}'.format(name))

    return value


def json_serial(obj):
    if isinstance(obj, Decimal):
        return float(obj)

    if isinstance(obj, (datetime, date, time)):
        return obj.isoformat()

    if is_dataclass(obj):
        return asdict(obj)

    raise TypeError("Type %s not serializable" % type(obj))


def get_pids(port):
    command = "sudo lsof -i :%s | awk '{print $2}'" % port
    pids = subprocess.check_output(command, shell=True)
    pids = pids.strip()
    if pids:
        pids = re.sub(' +', ' ', pids)
        for pid in pids.split('\n'):
            try:
                yield int(pid)
            except:
                pass
