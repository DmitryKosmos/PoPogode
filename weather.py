## encoding: utf-8
# подключаем библиотеку для работы с запросами
import requests
import weather_func





# указываем город
if __name__ == "__main__":
    city = "Москва"
    url = weather_func.get_url(city)



# формируем запрос
wd = temperature = temperature_min = temperature_max = temperature_sr = temperature_feels = sky = 0
# отправляем запрос на сервер и сразу получаем результат
def weather_data(url):
    global wd
    wd = requests.get(url).json()
    global temperature
    temperature = round(wd['main']['temp'])
    global temperature_min
    temperature_min = round(wd['main']['temp_min'])
    global temperature_max
    temperature_max = round(wd['main']['temp_max'])
    global temperature_sr
    temperature_sr = round((temperature_min + temperature_max) / 2)
    global temperature_feels
    temperature_feels = round(wd['main']['feels_like'])
    global sky
    sky = wd['weather'][0]['description']
    return wd, temperature, temperature_min, temperature_max, temperature_sr, temperature_feels, sky

# получаем данные о температуре и о том, как она ощущается


if __name__ == "__main__":
    weather_data(url)
    print('Сейчас в городе', city, str(temperature), '°C')
    print('Ощущается как', str(temperature_feels), '°C')
    print("min", temperature_min)
    print("max", temperature_max)
    print("sred", temperature_sr)
    print(sky)
    print(wd)  ##на всякий случай
