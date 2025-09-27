from flask import Blueprint, request, jsonify
from services.food_service import FoodService
from repositories.food_repository import FoodRepository

food_blueprint = Blueprint('foods', __name__)

# Инициализация зависимостей
food_repository = FoodRepository()
food_service = FoodService(food_repository)

@food_blueprint.route('/foods', methods=['GET'])
def get_foods():
    try:
        foods = food_service.get_all_foods()
        return jsonify([food.to_dict() for food in foods])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@food_blueprint.route('/foods/<int:id>', methods=['GET'])
def get_food(id):
    try:
        food = food_service.get_food_by_id(id)
        return jsonify(food.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@food_blueprint.route('/foods/brand/<string:brand>', methods=['GET'])
def get_foods_by_brand(brand):
    try:
        foods = food_service.get_foods_by_brand(brand)
        return jsonify([food.to_dict() for food in foods])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@food_blueprint.route('/foods/price', methods=['GET'])
def get_foods_by_price_range():
    try:
        min_price = float(request.args.get('min', 0))
        max_price = float(request.args.get('max', float('inf')))
        
        foods = food_service.get_foods_by_price_range(min_price, max_price)
        return jsonify([food.to_dict() for food in foods])
    except ValueError:
        return jsonify({'error': 'Неверный формат цены'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@food_blueprint.route('/foods/rating/<float:min_rating>', methods=['GET'])
def get_foods_by_rating(min_rating):
    try:
        if min_rating < 0 or min_rating > 5:
            return jsonify({'error': 'Рейтинг должен быть от 0 до 5'}), 400
            
        foods = food_service.get_foods_by_rating(min_rating)
        return jsonify([food.to_dict() for food in foods])
    except Exception as e:
        return jsonify({'error': str(e)}), 500