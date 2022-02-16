from server import routes
from flask_sqlalchemy import SQLAlchemy

from flask import Flask, jsonify
from flask_cors import CORS

from server.auth_class import AuthError

# Initiate the app
app = Flask(__name__)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "developmentSecretKey"
db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# Register blueprints
app.register_blueprint(routes.bp)
