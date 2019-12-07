from flask import make_response, jsonify, redirect

from locust_helper import create_app
from locust_helper.util.web_util import request_param

app = create_app()


# @app.after_request
# def after_request(response):
#     response.headers.set('Content-Type', 'application/json;charset=utf-8')
#     return response

@app.route('/hello', methods=['GET'])
def health():
    name = request_param("name")

    response = make_response(jsonify({"hello": name}))
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
