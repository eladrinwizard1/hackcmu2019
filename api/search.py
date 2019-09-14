from api import app
from api.sources import allrecipes_api as ar_api

@app.route('/search', methods=['POST'])
def search():
    pass
