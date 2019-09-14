class Recipe:
    def __init__(self, details: dict):
        self.ingredients = details['ingredients']
        self.time = details['total_time']
        self.rating = details['rating']
