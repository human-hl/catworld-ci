from models.cat import Cat

class CatRepository:
    def __init__(self):
        self.cats = [
            Cat(1, 'Мурзик', 'Британский', 3, 'Премиум корм'),
            Cat(2, 'Барсик', 'Сиамский', 2, 'Рыбный корм')
        ]
        self.next_id = 3

    def find_all(self):
        return self.cats.copy()

    def find_by_id(self, id):
        for cat in self.cats:
            if cat.id == id:
                return cat
        return None

    def create(self, cat):  
        new_cat = Cat(
            self.next_id,
            cat.name,          
            cat.breed,          
            cat.age,
            cat.favorite_food
        )
        self.cats.append(new_cat)
        self.next_id += 1
        return new_cat