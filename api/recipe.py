from api import app

@app.route('/recipe/<int:id>', methods=['GET'])
def recipe(id: int):
    pass
