import requests
from api import db_interface
import os
import json
from api.structs import Recipe
from typing import List

def search(ingredients: List[str]) -> List[int]:
    tot = ','.join(ingredients)
    response = requests.get(f"https://www.food2fork.com/api/search?key={os.environ['FOOD2FORK_ID']}&q={tot}")
    recipe_dict = json.loads(response.text)
    recipe_url_list = [recipe['f2f_url'] for recipe in recipe_dict['recipes']]
    return db_interface.add(recipe_url_list, 'food2fork')

def lookup(f2f_url: str) -> Recipe:
    index = f2f_url[f2f_url.rfind('/') + 1:]
    recipe_details = requests.get(f"https://www.food2fork.com/api/get?key={os.environ['FOOD2FORK_ID']}&rId={index}")
    recipe_details_list = json.loads(recipe_details.text).get('recipe')
    name = recipe_details_list.get('title')
    ingredients = recipe_details_list.get('ingredients')
    url = recipe_details_list.get('source_url')
    source = 'food2fork'
    return Recipe({ 'name' : name,
                    'ingredients' : ingredients, 
                    'url' : url, 
		    'source' : source})

