from models.cat import Cat
class CatService:
    def __init__(self, cat_repository):
        self.cat_repository = cat_repository

    def get_all_cats(self):
        try:
            return self.cat_repository.find_all()
        except Exception as e:
            raise Exception(f'Ошибка при получении списка котиков: {str(e)}')

    def get_cat_by_id(self, id):
        cat = self.cat_repository.find_by_id(id)
        if not cat:
            raise ValueError('Котик не найден')  
        return cat

    def create_cat(self, cat_data):
        if not cat_data.get('name') or not cat_data.get('breed'):
            raise ValueError('Имя и порода обязательны для заполнения')
        
        if not isinstance(cat_data.get('age', 0), int) or cat_data['age'] < 0:
            raise ValueError('Возраст должен быть положительным числом')
        
        new_cat = Cat(
            None, 
            cat_data['name'],
            cat_data['breed'],
            cat_data['age'],
            cat_data.get('favorite_food', '')
        )
        return self.cat_repository.create(new_cat)  