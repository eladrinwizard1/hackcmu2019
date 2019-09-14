import os
import json
import requests
from api import db_interface
from api.structs import Recipe
from typing import List

def search(ingredients: List[str]) -> List[int]:
    tot = ',+'.join(ingredients)
    response = requests.get(f"https://api.edamam.com/search?q={tot}&app_id={os.environ['EDAMAM_ID']}&app_key={os.environ['EDAMAM_KEY']}")
    recipe_dict = json.loads(response.text)
    recipe_url_list = [recipe['recipe']['url'] for recipe in recipe_dict['hits']]
    return db_interface.add(recipe_url_list, 'edamam')

def lookup(url: str) -> Recipe:
    response = requests.get(f"https://api.edamam.com/search?r={url}&app_id={os.environ['EDAMAM_ID']}&app_key={os.environ['EDAMAM_KEY']}")
    recipe_details = json.loads(response.text)['recipe']
    name = recipe_details.get('label')
    ingredients = recipe_details.get('ingredients')
    return Recipe(name, ingredients)
