from flask import Blueprint, jsonify, request
from server.auth_class import requires_auth
from flask_cors import cross_origin

bp = Blueprint('routes', __name__, url_prefix="")

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


@bp.route('/get-recipes', methods=['GET'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_recipes():
    return jsonify({'status': 'success', 'recipes': recipes})


@bp.route('/get-recipes-general', methods=['GET'])
@cross_origin(headers=["Content-Type"])
def get_recipes_general():
    return jsonify({'status': 'success', 'recipes': recipes_general})


@bp.route('post-recipe', methods=['POST'])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def post_recipes():
    print(request)
    return jsonify({'status': 'success'})
