## encoding: utf-8
# подключаем библиотеку для работы с запросами
import requests
import user_add

def get_last_user_city():
    try:
        with open('users.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                last_user_city = last_line.split(',')[1]
                return last_user_city
            else:
                return 505
    except FileNotFoundError:
        print("Файл 'users.txt' не найден.")
        return "Нет файла"
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return "Ошибка"

# указываем город
if __name__ == "__main__":
    city = 'Москва'
else:
    city = get_last_user_city()

# формируем запрос
url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid=3f472b11c2822d4d48af1c44a7ad2d5e'
# отправляем запрос на сервер и сразу получаем результат
weather_data = requests.get(url).json()
# получаем данные о температуре и о том, как она ощущается
temperature = round(weather_data['main']['temp'])
temperature_min = round(weather_data['main']['temp_min'])
temperature_max = round(weather_data['main']['temp_max'])
temperature_sr = round((temperature_min + temperature_max) / 2)
temperature_feels = round(weather_data['main']['feels_like'])
sky = weather_data['weather'][0]['description']

if __name__ == "__main__":
    print('Сейчас в городе', city, str(temperature), '°C')
    print('Ощущается как', str(temperature_feels), '°C')
    print("min", temperature_min)
    print("max", temperature_max)
    print("sred", temperature_sr)
    print(sky)
    print(weather_data)  ##на всякий случай
