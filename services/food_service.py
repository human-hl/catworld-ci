from models.food import Food
class FoodService:
    def __init__(self, food_repository):
        self.food_repository = food_repository

    def get_all_foods(self):
        try:
            return self.food_repository.find_all()
        except Exception as e:
            raise Exception(f'Ошибка при получении списка кормов: {str(e)}')

    def get_food_by_id(self, id):
        food = self.food_repository.find_by_id(id)
        if not food:
            raise Exception('Корм не найден')
        return food

    def get_foods_by_brand(self, brand):
        try:
            all_foods = self.food_repository.find_all()
            return [food for food in all_foods if food.brand.lower() == brand.lower()]
        except Exception as e:
            raise Exception(f'Ошибка при поиске кормов по бренду: {str(e)}')

    def get_foods_by_price_range(self, min_price, max_price):

        if min_price > max_price:
            raise ValueError('Минимальная цена должна быть меньше максимальной')
        if min_price < 0 or max_price < 0:
            raise ValueError('Цены должны быть положительными')
        
        try:
            all_foods = self.food_repository.find_all()
            return [food for food in all_foods if min_price <= food.price <= max_price]
        except Exception as e:
            raise Exception(f'Ошибка при поиске кормов по цене: {str(e)}')

    def get_foods_by_rating(self, min_rating):

        if min_rating < 0 or min_rating > 5:
            raise ValueError('Рейтинг должен быть между 0 и 5')
        
        try:
            all_foods = self.food_repository.find_all()
            return [food for food in all_foods if food.rating >= min_rating]
        except Exception as e:
            raise Exception(f'Ошибка при поиске кормов по рейтингу: {str(e)}')