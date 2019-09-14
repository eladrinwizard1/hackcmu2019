import requests
import db_interface
import os
import json
from typing import List

def search(ingredients: List[str]) -> List[int]:
    tot = ',+'.join(ingredients)
    response = requests.get(f"https://api.edamam.com/search?q={tot}&app_id={os.environ['EDAMAM_ID']}&app_key={os.environ['EDAMAM_KEY']}")
    recipe_dict = json.loads(response.text)
    recipe_url_list = []
    for recipe in recipe_dict:
        recipe_url_list.append(recipe['url'])
    print(recipe_url_list)
