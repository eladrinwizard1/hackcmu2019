from allrecipes import AllRecipes as ar
from models import Recipe
import db_interface
from typing import List

def search(ingredients: List[str]) -> List[int]:
    query_options = {
        'ingIncl' : ' '.join(ingredients),
        'sort' : 'p'
    }
    query_results = ar.search(query_options)
    return db_interface.add([recipe['url'] for recipe in query_results])

def lookup(url: str) -> Recipe:
    recipe_details = ar.get(url)
    return Recipe(recipe_details)
