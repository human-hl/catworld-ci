import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

from repositories.cat_repository import CatRepository
from repositories.food_repository import FoodRepository
from services.cat_service import CatService
from services.food_service import FoodService

class TestServiceRepositoryIntegration:
    """Интеграционные тесты сервисов и репозиториев"""
    
    def setup_method(self):
        self.cat_repo = CatRepository()
        self.food_repo = FoodRepository()
        self.cat_service = CatService(self.cat_repo)
        self.food_service = FoodService(self.food_repo)
    
    def test_cat_service_get_all(self):
        cats = self.cat_service.get_all_cats()
        assert len(cats) == 2
        assert cats[0].name == "Мурзик"
    
    def test_cat_service_get_by_id(self):
        cat = self.cat_service.get_cat_by_id(1)
        assert cat.name == "Мурзик"
        
        with pytest.raises(ValueError):
            self.cat_service.get_cat_by_id(999)
    
    def test_cat_service_create_valid(self):
        cat_data = {
            'name': 'Тестовый',
            'breed': 'Тестовая', 
            'age': 2,
            'favorite_food': 'Тест'
        }
        
        new_cat = self.cat_service.create_cat(cat_data)
        assert new_cat.name == 'Тестовый'
        assert new_cat.id == 3
    
    def test_cat_service_create_invalid(self):
        invalid_data = {'name': '', 'breed': 'Тест'}
        
        with pytest.raises(ValueError):
            self.cat_service.create_cat(invalid_data)
    
    def test_food_service_price_range(self):
        foods = self.food_service.get_foods_by_price_range(1000, 2000)
        assert len(foods) == 2
        
        with pytest.raises(ValueError):
            self.food_service.get_foods_by_price_range(2000, 1000)