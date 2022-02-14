import os

from flask import Flask, jsonify
from flask_cors import CORS


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',  # Change to a random key when in production
        DATABASE=os.path.join(app.instance_path, 'database.sqlite'),
    )

    # enable CORS
    # Change this when in production to only allow access from the client.
    CORS(app, resources={r'/*': {'origins': '*'}})

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Add the database
    from . import db
    db.init_app(app)

    from . import recipes
    app.register_blueprint(recipes.bp)

    return app
