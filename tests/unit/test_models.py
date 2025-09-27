import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from models.cat import Cat
from models.food import Food

class TestModels:
    """Тесты моделей с использованием pytest"""
    
    def test_cat_creation(self):
        cat = Cat(1, "Мурзик", "Британский", 3, "Pro Plan")
        assert cat.name == "Мурзик"
        assert cat.breed == "Британский"
        assert cat.age == 3
        
    def test_cat_to_dict(self):
        cat = Cat(1, "Мурзик", "Британский", 3, "Pro Plan")
        cat_dict = cat.to_dict()
        assert cat_dict['name'] == "Мурзик"
        assert cat_dict['id'] == 1
        
    def test_food_creation(self):
        food = Food(1, "Pro Plan", "Purina", 1200, 4.5)
        assert food.name == "Pro Plan"
        assert food.price == 1200
        assert food.rating == 4.5