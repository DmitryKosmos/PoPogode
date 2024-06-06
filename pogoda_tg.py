import os
import telebot
from telebot import types
import pop

# Токен вашего бота
API_TOKEN = '6928765752:AAHY5e0iUdiEWRIMkZmskbiqMKb7_AYTrjg'

# Создание экземпляра бота
bot = telebot.TeleBot(API_TOKEN)

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

# Функция для сохранения информации о пользователе
def save_user_info(user_id, city):
    with open(users_file, 'a') as f:
        f.write(f'{user_id},{city}\n')

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
        pop.get_weather(user_city)
    else:
        bot.send_message(user_id, 'Пожалуйста, сначала установите ваш город.')


# Обработчик нажатия на кнопку "Сменить город"
@bot.message_handler(func=lambda message: message.text == 'Сменить город')
def change_city(message):
    user_id = message.chat.id
    msg = bot.reply_to(message, 'Введите новый город:')
    bot.register_next_step_handler(msg, save_city)

# Запуск бота
bot.polling()
