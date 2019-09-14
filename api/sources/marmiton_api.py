from marmiton import Marmiton as mr
from api import db_interface
from api.structs.recipe import Recipe
from typing import List

def search(ingredients: List[str]) -> List[int]:
    query_options = {
        'aqt' : ' '.join(ingredients),
    }
    query_results = mr.search(query_options)
    return db_interface.add([recipe['url'] for recipe in query_results], 'marmiton')

def lookup(url: str) -> Recipe:
    recipe_details = mr.get(url)
    name = recipe_details.get('name')
    ingredients = recipe_details.get('ingredients')
    time = recipe_details.get('total_time')
    image = recipe_details.get('image')
    rating = recipe_details.get('rate')
    return Recipe({ 'name' : name,
                    'ingredients' : ingredients,
                    'time' : time,
                    'image' : image,
                    'rating' : rating,
                    'url' : url
                    })
