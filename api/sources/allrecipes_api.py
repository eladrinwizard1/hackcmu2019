from allrecipes import AllRecipes as ar
import db_interface
from typing import List

def search(ingredients: List[str]) -> List[int]:
    query_options = {
        'ingIncl' : ' '.join(ingredients),
        'sort' : 'p'
    }
    query_results = ar.search(query_options)
    return db_interface.add([recipe['url'] for recipe in query_results])

def get(ident: int) -> Recipe:
    pass
