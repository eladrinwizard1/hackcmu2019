from api import app

@app.route('/ingredient/<string:query>', methods=['GET'])
def ingredient(query: str):
    pass
