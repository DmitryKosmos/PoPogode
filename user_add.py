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

if __name__ == "__main__":
    # Пример использования функции
    delete_user_from_txt(input("Кого удалить: "))
    # Пример использования функции
    add_user_to_txt(input("Имя: "), input("Город: "))

