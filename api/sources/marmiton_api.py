from marmiton import Marmiton
from api import db_interface
from api.structs.recipe import Recipe
from typing import List

def search(ingredients: List[str]) -> List[int]:
    query_options = {
        'aqt' : ' '.join(ingredients),
    }
    query_results = Marmiton.search(query_options)
    return db_interface.add([recipe['url'] for recipe in query_results], 'marmiton')

def lookup(url: str) -> Recipe:
    recipe_details = ar.get(url)
    name = recipe_details.get('name')
    ingredients = recipe_details.get('ingredients')
    time = recipe_details.get('total_time')
    rating = recipe_details.get('rate')
    return Recipe({ 'name' : name,
                    'ingredients' : ingredients,
                    'time' : time,
                    'rating' : rating})
