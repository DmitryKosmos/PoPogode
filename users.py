class User():
    def __init__(self, name, city):
        self.name = name
        self.city = city

moskvich = User("Москвич", "Москва")


def add_user():
    new_user_name = input(str("Введите имя: ", ))
    new_user_city = input(str("Введите город: ", ))
    new_user = User(new_user_name, new_user_city)


