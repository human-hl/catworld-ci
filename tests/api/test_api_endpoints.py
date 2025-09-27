import requests
import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))

class TestAPIEndpoints:
    """Тесты API endpoints с использованием pytest"""
    
    BASE_URL = "http://127.0.0.1:5000/api"
    
    def test_get_cats(self):
        response = requests.get(f"{self.BASE_URL}/cats")
        assert response.status_code == 200
        cats = response.json()
        assert isinstance(cats, list)
        assert len(cats) > 0
    
    def test_get_cat_by_id(self):
        response = requests.get(f"{self.BASE_URL}/cats/1")
        assert response.status_code == 200
        cat = response.json()
        assert cat['id'] == 1
    
    def test_get_nonexistent_cat(self):
        response = requests.get(f"{self.BASE_URL}/cats/999")
        assert response.status_code == 404
    
    def test_create_cat(self):
        new_cat = {
            'name': 'API Тест',
            'breed': 'Тестовая',
            'age': 1,
            'favorite_food': 'Тест'
        }
        
        response = requests.post(
            f"{self.BASE_URL}/cats",
            json=new_cat,
            headers={'Content-Type': 'application/json'}
        )
        
        assert response.status_code == 201
        created_cat = response.json()
        assert created_cat['name'] == 'API Тест'
    
    def test_create_invalid_cat(self):
        invalid_cat = {'name': ''}
        
        response = requests.post(
            f"{self.BASE_URL}/cats", 
            json=invalid_cat,
            headers={'Content-Type': 'application/json'}
        )
        
        assert response.status_code == 400
    
    def test_get_foods(self):
        response = requests.get(f"{self.BASE_URL}/foods")
        assert response.status_code == 200
        foods = response.json()
        assert isinstance(foods, list)