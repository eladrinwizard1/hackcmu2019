class Recipe:
    def __init__(self, details: dict):
        self.name = details.get('name')
        self.ingredients = details.get('ingredients')
        self.time = details.get('time')
        self.rating = details.get('rating')

    def to_dict(self):
        return {
                'name' : self.name,
                'ingredients' : self.ingredients,
                'time' : self.time,
                'rating' : self.rating
                }
