import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from repositories.cat_repository import CatRepository
from repositories.food_repository import FoodRepository
from models.cat import Cat
from models.food import Food

class TestRepositories:
    """Тесты репозиториев с использованием pytest"""
    
    def setup_method(self):
        self.cat_repo = CatRepository()
        self.food_repo = FoodRepository()
    
    def test_find_all_cats(self):
        cats = self.cat_repo.find_all()
        assert len(cats) == 2
        assert cats[0].name == "Мурзик"
    
    def test_find_cat_by_id(self):
        cat = self.cat_repo.find_by_id(1)
        assert cat is not None
        assert cat.name == "Мурзик"
        
        cat_none = self.cat_repo.find_by_id(999)
        assert cat_none is None
    
    def test_create_cat(self):
        new_cat = Cat(None, "Тестовый", "Тестовая", 1, "Тест")
        created_cat = self.cat_repo.create(new_cat)
        
        assert created_cat.id == 3
        assert created_cat.name == "Тестовый"
        assert len(self.cat_repo.find_all()) == 3