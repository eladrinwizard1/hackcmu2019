from api import app
from api.sources import allrecipes_api as ar_api
from api.sources import edamam_api as ed_api
from flask import jsonify
from flask import request

@app.route('/search', methods=['POST'])
def search():
    ingredients = request.json['ingredients']
    ids = []
    ids.extend(ed_api.search(ingredients))
    return jsonify(ids)
