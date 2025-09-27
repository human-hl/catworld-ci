# repositories/food_repository.py
from models.food import Food

class FoodRepository:
    def __init__(self):
        self.foods = [
            Food(1, 'Pro Plan', 'Purina', 1200, 4.5),
            Food(2, 'Whiskas', 'Mars', 500, 3.8),
            Food(3, 'Royal Canin', 'Royal Canin', 1500, 4.7)
        ]
        self.next_id = 4

    def find_all(self):
        return self.foods.copy()

    def find_by_id(self, id):
        for food in self.foods:
            if food.id == id:
                return food
        return None

    def find_by_brand(self, brand):
        return [food for food in self.foods if food.brand.lower() == brand.lower()]

    def find_by_price_range(self, min_price, max_price):
        return [food for food in self.foods if min_price <= food.price <= max_price]

    def find_by_rating(self, min_rating):
        return [food for food in self.foods if food.rating >= min_rating]

    def create(self, food):
        new_food = Food(
            self.next_id,
            food.name,
            food.brand,
            food.price,
            food.rating
        )
        self.foods.append(new_food)
        self.next_id += 1
        return new_food