from marmiton import Marmiton
import api.db_interface
from api.structs import Recipe
from typing import List

def search(ingredients: List[str]) -> List[int]:
    query_options = {
        'aqt' : ' '.join(ingredients),
    }
    query_results = Marmiton.search(query_options)
    return db_interface.add([recipe['url'] for recipe in query_results])

def lookup(url: str) -> Recipe:
    recipe_details = ar.get(url)
    name = recipe_details['name']
    ingredients = recipe_details['ingredients']
    time = recipe_details['total_time']
    rating = recipe_details['rate']
    return Recipe(name, ingredients, time, rating)
