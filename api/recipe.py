from api import app
from api import db_interface
from api.sources import allrecipes_api as ar_api
from api.sources import edamam_api as ed_api
from api.sources import marmiton_api as m_api
from api.sources import nutritionix_api as n_api
from flask import jsonify

@app.route('/recipe/<int:id>', methods=['GET'])
def recipe(id: int):
    source, url = db_interface.get(id)
    detailed_info = None
    if source == 'allrecipes':
        detailed_info = ar_api.lookup(url)
    elif source == 'edamam':
        detailed_info = ed_api.lookup(url)
    elif source == 'marmiton':
        detailed_info = m_api.lookup(url)
    elif source == 'nutritionix':
        detailed_info = n_api.lookup(url)
    # etc...
    return jsonify(detailed_info.to_dict())
