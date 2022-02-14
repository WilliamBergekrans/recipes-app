from flask import Blueprint, jsonify
from itsdangerous import json

bp = Blueprint('recipes', __name__, url_prefix='/recipes')

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


@ bp.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@ bp.route('/get-recipes', methods=['GET'])
def get_recipes():
    return jsonify({'status': 'success', 'recipes': recipes})
