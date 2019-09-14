from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from api import search, ingredient, recipe, errors, sources, structs, db_interface
