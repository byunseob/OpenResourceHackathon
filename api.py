import subprocess
import logging
from flask import Blueprint, app, redirect
from flask_cors import cross_origin

from locust_helper.template import get_template
from locust_helper.util.web_util import request_json

locust_bp = Blueprint('locust_bp', __name__)

logger = logging.getLogger("locust")


@locust_bp.route('', methods=['GET'])
@cross_origin()
def index():
    return redirect("http://localhost:8089")


@locust_bp.route('', methods=['POST'])
@cross_origin()
def create():
    method = request_json('method', required=True)
    host = request_json('host', required=True)
    params = request_json('params')
    headers = request_json('headers')
    body = request_json('body')

    with open('_locust.py', 'w') as opened_file:
        opened_file.write(get_template(method=method,
                                       params=params,
                                       headers=headers,
                                       body=body,
                                       min_wait=1000,
                                       max_wait=1000))

    try:
        subprocess.call(f"locust -f _locust.py --host={host} &", shell=True)
    except subprocess.CalledProcessError as e:
        logger.error(e)

    return "success"


@locust_bp.route('', methods=['DELETE'])
@cross_origin()
def delete():
    try:
        subprocess.call(f"curl -X GET http://localhost:8089/stop", shell=True)
    except subprocess.CalledProcessError as e:
        logger.error(e)

    return "success"
