import os
import telebot
from telebot import types
## weather
import pop
import weather_func
import re


# Создание экземпляра бота
bot = telebot.TeleBot("6928765752:AAHY5e0iUdiEWRIMkZmskbiqMKb7_AYTrjg")

# Путь к файлу users.txt
users_file = 'users.txt'

# Функция для получения города пользователя
def get_user_city(user_id):
    if os.path.isfile(users_file):
        with open(users_file, 'r') as f:
            for line in f:
                user_info = line.strip().split(',')
                if str(user_id) == user_info[0]:
                    return user_info[1]
    return None

correct_cities = weather_func.correct_cities
def save_user_info(user_id, city):
    # Проверяем, что город введен на русском языке
    if not re.match(r'^[а-яА-ЯёЁ\s]+$', city):
        print("Город должен быть введен на русском языке.")
        return

    # Проверяем, что город написан правильно
    city_lower = city.lower()
    if city_lower not in correct_cities:
        print(f"Город '{city}' не найден или введен неправильно.")
        return
    corrected_city = correct_cities[city_lower]

    # Проверяем, есть ли запись для этого пользователя
    user_data = read_user_data()
    updated_user_data = []
    found_user = False

    for line in user_data:
        parts = line.split(',')
        if len(parts) == 2:
            line_user_id, line_city = parts
            if line_user_id == str(user_id):
                found_user = True
                # Обновляем существующую запись
                updated_user_data.append(f'{user_id},{corrected_city}')
            else:
                updated_user_data.append(line)

    # Если пользователь не найден, добавляем новую запись
    if not found_user:
        updated_user_data.append(f'{user_id},{corrected_city}')

    # Сохраняем обновленные данные в файл
    with open(users_file, 'w') as f:
        for line in updated_user_data:
            f.write(f'{line}\n')



def read_user_data():
    user_data = []
    try:
        with open(users_file, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    user_id, city = parts
                    user_data.append(f'{user_id},{city}')
                else:
                    print(f'Некорректная строка в файле: {line.strip()}')
    except FileNotFoundError:
        pass
    return user_data


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    user_city = get_user_city(user_id)

    if user_city is None:
        msg = bot.reply_to(message, 'Введите ваш город:')
        bot.register_next_step_handler(msg, save_city)
    else:
        bot.send_message(user_id, f'Ваш город: {user_city}')
        show_main_menu(message)

# Обработчик сохранения города
def save_city(message):
    user_id = message.chat.id
    city = message.text
    if not re.match(r'^[а-яА-ЯёЁ\s]+$', city):
        bot.send_message(user_id, "Город должен быть введен на русском языке.")
        return

    # Проверяем, что город написан правильно
    city_lower = city.lower()
    if city_lower not in correct_cities:
        bot.send_message(user_id, f"Город '{city}' не найден или введен неправильно.")
        return
    corrected_city = correct_cities[city_lower]
    save_user_info(user_id, city)
    bot.send_message(user_id, f'Город сохранен: {city}')
    show_main_menu(message)

# Функция для отображения главного меню
def show_main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Узнать погоду')
    btn2 = types.KeyboardButton('Сменить город')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Выберите действие:', reply_markup=markup)


# Обработчик нажатия на кнопку "Узнать погоду"
@bot.message_handler(func=lambda message: message.text == 'Узнать погоду')
def get_weather(message):
    user_id = message.chat.id

    user_city = get_user_city(user_id)
    if user_city is not None:
        url = weather_func.get_url(user_city)
        proghoz = str(pop.get_weather(url))
        podrobnee = str(pop.popodrobnee(user_city))
        bot.send_message(user_id, proghoz + "\n" + podrobnee)
    else:
        bot.send_message(user_id, 'Пожалуйста, сначала установите ваш город.')


# Обработчик нажатия на кнопку "Сменить город"
@bot.message_handler(func=lambda message: message.text == 'Сменить город')
def change_city(message):
    user_id = message.chat.id
    msg = bot.reply_to(message, 'Введите новый город:')
    bot.register_next_step_handler(msg, save_city)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'тест' or message.text == 'test' or message.text == "Где я?"\
            or message.text == "где я?":
        user_id = message.chat.id
        user_city = get_user_city(user_id)
        bot.send_message(user_id, user_city)

# Запуск бота
bot.polling()
