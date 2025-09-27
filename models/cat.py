class Cat:
    def __init__(self, id, name, breed, age, favorite_food):
        self.id = id
        self.name = name
        self.breed = breed
        self.age = age
        self.favorite_food = favorite_food
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'breed': self.breed,
            'age': self.age,
            'favorite_food': self.favorite_food
        }