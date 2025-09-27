from flask import Blueprint, request, jsonify
from services.cat_service import CatService
from repositories.cat_repository import CatRepository

cat_blueprint = Blueprint('cats', __name__)

cat_repository = CatRepository()
cat_service = CatService(cat_repository)

@cat_blueprint.route('/cats', methods=['GET'])
def get_cats():
    try:
        cats = cat_service.get_all_cats()
        return jsonify([cat.to_dict() for cat in cats])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@cat_blueprint.route('/cats/<int:id>', methods=['GET'])
def get_cat(id):
    try:
        cat = cat_service.get_cat_by_id(id)
        return jsonify(cat.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@cat_blueprint.route('/cats', methods=['POST'])
def create_cat():
    try:
        cat_data = request.get_json()
        new_cat = cat_service.create_cat(cat_data)
        return jsonify(new_cat.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400