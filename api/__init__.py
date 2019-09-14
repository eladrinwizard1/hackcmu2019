from flask import Flask

app = Flask(__name__)

from api import search, ingredient, recipe, errors, sources, structs, db_interface
