class Food:
    def __init__(self, id, name, brand, price, rating):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.rating = rating
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'price': self.price,
            'rating': self.rating
        }