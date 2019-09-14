from allrecipes import AllRecipes as ar
from api.structs import Recipe
from api import db_interface
from typing import List

def search(ingredients: List[str]) -> List[int]:
    query_options = {
        'ingIncl' : ' '.join(ingredients),
        'sort' : 'p'
    }
    query_results = ar.search(query_options)
    return db_interface.add([recipe['url'] for recipe in query_results], 'allrecipes')

def lookup(url: str) -> Recipe:
    recipe_details = ar.get(url)
    name = recipe_details['name']
    ingredients = recipe_details['ingredients']
    time = recipe_details['total_time']
    rating = recipe_details['rating'] 
    return Recipe(name, ingredients, time, rating)
