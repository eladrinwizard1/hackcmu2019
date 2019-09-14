from allrecipes import AllRecipes as ar

def search(ingredients: List[str]) -> List[dict]:
    query_options = {
        "ingIncl" : " ".join(ingredients),
    }
    print(ar.search(query_options))
