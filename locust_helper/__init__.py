
from flask import Flask
from flask_cors import CORS


def create_app():
    """
    Create flask app
    :return: flask app
    """
    app = Flask(__name__)
    CORS(app)
    context_path = '/locust'

    from locust_helper.api import locust_bp

    app.register_blueprint(locust_bp, url_prefix='{}'.format(context_path))

    return app
