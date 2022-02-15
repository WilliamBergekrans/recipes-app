from flask_sqlalchemy import SQLAlchemy
import json

from urllib.request import urlopen
from functools import wraps

from flask import Flask, request, jsonify, _request_ctx_stack
from flask_cors import cross_origin, CORS
from jose import jwt

# Initiate the app
app = Flask(__name__)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = "developmentSecretKey"
db = SQLAlchemy(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Error handler
AUTH0_DOMAIN = 'dev-ey7752fa.eu.auth0.com'
API_AUDIENCE = "http://127.0.0.1:5000/"
ALGORITHMS = ["RS256"]


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

# /server.py

# Format error response and append status code


def get_token_auth_header():
    """Obtains the Access Token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token


def requires_auth(f):
    """Determines if the Access Token is valid
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = get_token_auth_header()
        jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
        print(jsonurl)
        jwks = json.loads(jsonurl.read())
        unverified_header = jwt.get_unverified_header(token)
        rsa_key = {}
        for key in jwks["keys"]:
            if key["kid"] == unverified_header["kid"]:
                rsa_key = {
                    "kty": key["kty"],
                    "kid": key["kid"],
                    "use": key["use"],
                    "n": key["n"],
                    "e": key["e"]
                }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer="https://"+AUTH0_DOMAIN+"/"
                )
            except jwt.ExpiredSignatureError:
                raise AuthError({"code": "token_expired",
                                "description": "token is expired"}, 401)
            except jwt.JWTClaimsError:
                raise AuthError({"code": "invalid_claims",
                                "description":
                                    "incorrect claims,"
                                    "please check the audience and issuer"}, 401)
            except Exception:
                raise AuthError({"code": "invalid_header",
                                "description":
                                    "Unable to parse authentication"
                                    " token."}, 401)

            _request_ctx_stack.top.current_user = payload
            return f(*args, **kwargs)
        raise AuthError({"code": "invalid_header",
                        "description": "Unable to find appropriate key"}, 401)
    return decorated


recipes = [{
    "name": "Lasagne",
    "description": "Klassisk lasagne är väl en rätt man aldrig tröttnar på? Med det här receptet blir din lasagne perfekt med en mjuk och härlig konsistens och dessutom har den en ljuv och exemplarisk smak. Parmesanosten är pricken över i!"
},
    {
    "name": "Grönsaksbiffar",
    "description": "En klassisk vegetarisk biffrätt som är god och nyttig för alla tillfällen. Kommer bli god!"
},
    {
    "name": "Pannkor",
    "description": "Vem älskar inte pannkakor? Det klassiska receptet för en lyckad brunch"
},
    {
    "name": "Het linspasta med oregano",
    "description": "En fräsch pasta kommer här med dofter och smaker från oregano, tomat och chili. Grädden tillför det där krämiga och soltorkade tomaterna det där syrliga och smakrika. Klart på under 30 minuter.!"
},
    {
    "name": "Enkel moussaka",
    "description": "En saftig och riktigt god moussaka med aubergine och blandfärs. Moussakan görs enkelt med färdig potatisgratäng som grund. En svensk version av en härlig grekisk klassiker."
}]


recipes_general = [{
    "name": "Lasagne",
    "description": "Klassisk lasagne är väl en rätt man aldrig tröttnar på? Med det här receptet blir din lasagne perfekt med en mjuk och härlig konsistens och dessutom har den en ljuv och exemplarisk smak. Parmesanosten är pricken över i!"
},
    {
    "name": "Grönsaksbiffar",
    "description": "En klassisk vegetarisk biffrätt som är god och nyttig för alla tillfällen. Kommer bli god!"
}]


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/get-recipes', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_recipes():
    return jsonify({'status': 'success', 'recipes': recipes})


@app.route('/get-recipes-general', methods=['GET'])
@cross_origin(headers=["Content-Type"])
def get_recipes_general():
    return jsonify({'status': 'success', 'recipes': recipes_general})
