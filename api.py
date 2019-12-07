import subprocess
import os
import re
import logging
from flask import Blueprint, redirect, render_template
from flask_cors import cross_origin

from locust_helper.template import get_template
from locust_helper.util.web_util import request_json, request_param

locust_bp = Blueprint('locust_bp', __name__)

logger = logging.getLogger("locust")


@locust_bp.route('/form', methods=['GET'])
def home():
    host = request_param('host', required=True)
    return render_template('index.html', host=host)

# @locust_bp.route('', methods=['GET'])
# @cross_origin()
# def index():
#     host = request_param('host', required=True)
#     return redirect(f"http://{host}:8089")

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
                                       min_wait=1,
                                       max_wait=1))
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
        pids = set(get_pids(8089))
        command = 'sudo kill -9 {}'.format(' '.join([str(pid) for pid in pids]))
        os.system(command)
    except subprocess.CalledProcessError as e:
        logger.exception(e)
    except Exception as e:
        logger.exception(e)

    return "success"


def get_pids(port):
    command = "lsof -i :%s | awk '{print $2}'" % port
    pids = subprocess.check_output(command, shell=True)
    pids = pids.strip()
    if pids:
        pids = re.sub(' +', ' ', pids)
        for pid in pids.split('\n'):
            try:
                print(pid)
                yield int(pid)
            except:
                pass
