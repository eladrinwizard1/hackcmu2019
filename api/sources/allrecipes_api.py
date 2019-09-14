from allrecipes import AllRecipes as ar
from api.structs.recipe import Recipe
from api import db_interface
from typing import List

def search(ingredients: List[str]) -> List[int]:
    query_options = {
        'ingIncl' : ' '.join(ingredients),
        'sort' : 'p'
    }
    try:
        query_results = ar.search(query_options)
    except StopIteration:
        print("No results found on allrecipes")
        return []
    return db_interface.add([recipe['url'] for recipe in query_results], 'allrecipes')

def lookup(url: str) -> Recipe:
    recipe_details = ar.get(url)
    name = recipe_details.get('name')
    ingredients = recipe_details.get('ingredients')
    time = recipe_details.get('total_time')
    rating = recipe_details.get('rating')
    return Recipe({ 'name' : name,
                    'ingredients' : ingredients,
                    'time' : time,
                    'rating' : rating})
