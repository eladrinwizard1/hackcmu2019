import requests
import api.db_interface
import os
import json
from typing import List


#I can't make a usable api key


def search(ingredients: List[str]) -> List[int]:
    tot = ',+'.join(ingredients)
    response = requests.get(f"https://api.spoonacular.com/recipes/search?query={tot}&number=2?apiKey={os.environ['SPOONACULAR_KEY']}")
    recipe_dict = json.loads(response.text)
    print(recipe_dict)
    #recipe_url_list = [recipe['id'] for recipe in recipe_dict]
    #print(recipe_url_list)
    #return db_interface.add(recipe_url_list)

