import requests
import db_interface
import os
import json
from typing import List

def search(ingredients: List[str]) -> List[int]:
    tot = ','.join(ingredients)
    response = requests.get(f"http://www.recipepuppy.com/api/?i={tot}") 
    recipe_dict = json.loads(response.text)
    recipe_url_list = [recipe['href'] for recipe in recipe_dict['results']]
    return db_interface.add(recipe_url_list)


