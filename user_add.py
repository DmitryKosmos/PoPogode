class user():
    def __init__(self, user_name, user_city):
        self.user_name = user_name
        self.user_city = user_city




def add_user_to_txt(user_name, user_city):
    # Создание строки для записи в файл
    user_data = f"{user_name}\t{user_city}\n"

    # Открываем txt файл в режиме добавления ('a')
    with open('users.txt', mode='a') as file:
        # Записываем данные нового пользователя в файл
        file.write(user_data)


def delete_user_from_txt(user_name):
    # Открываем txt файл для чтения и запоминаем его содержимое
    with open('users.txt', mode='r') as file:
        lines = file.readlines()

    # Открываем txt файл для записи и перезаписываем его содержимое
    with open('users.txt', mode='w') as file:
        for line in lines:
            # Разделяем строку на имя и город по табуляции
            values = line.strip().split('\t')

            # Проверяем, если имя пользователя совпадает с удаляемым именем, то пропускаем запись
            if values[0] == user_name:
                continue

            # Записываем оставшиеся данные обратно в файл
            file.write(line)


def get_city_by_name(user_name):
    # Открываем txt файл для чтения
    with open('users.txt', mode='r') as file:
        for line in file:
            # Разделяем строку на имя и город по табуляции
            values = line.strip().split('\t')

            # Проверяем, если имя пользователя совпадает с искомым именем, то присваиваем город переменной city
            if values[0] == user_name:
                city = values[1]
                return city

    # Если пользователь не был найден, запрашиваем у пользователя, добавить ли его в файл
    qwestion = input("Такого пользователя нет. Добавить? ")
    if qwestion == "Да" or qwestion == "да":
        add_user_to_txt(input("Имя: "), input("Город: "))
        return get_city_by_name(user_name)  # Вызываем функцию заново, чтобы получить город для добавленного пользователя
    else:
        return None  # Возвращаем None, если пользователь отказался добавлять нового пользователя



if __name__ == "__main__":
    # Пример использования функции
    delete_user_from_txt(input("Кого удалить: "))
    # Пример использования функции
    add_user_to_txt(input("Имя: "), input("Город: "))
    # Пример использования функции
    user_city = get_city_by_name("John")
    if user_city:
        print(f"The city for John is: {user_city}")
    else:
        print("User not found.")

