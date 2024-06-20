## encoding: utf-8
# подключаем библиотеку для работы с запросами
import requests
import weather_func





# указываем город
if __name__ == "__main__":
    city = "Москва"
    url = weather_func.get_weather(city)
else:
    city = input(str("Введите город: "))
    url = weather_func.get_weather(city)

# формируем запрос

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
