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
    recipe_details = ar.get(url)
    name = recipe_details['name']
    ingredients = recipe_details['ingredients']
    time = recipe_details['total_time']
    rating = recipe_details['rating']
    return Recipe(name, ingredients, time, rating)
