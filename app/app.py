from flask import Flask


def create_app():
    """
    Create app flask
    :return: new app
    """
    new_app = Flask(__name__)
    new_app.debug = True
    new_app.config['JSON_SORT_KEYS'] = False

    return new_app


app = create_app()