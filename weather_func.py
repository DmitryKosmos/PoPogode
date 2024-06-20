## encoding: utf-8
# подключаем библиотеку для работы с запросами
import requests
import pop

city_u = ""
def get_city(city):
    global city_u
    city_u = city
    return city_u
def get_url(city_u):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city_u + '&units=metric&lang=ru&appid=3f472b11c2822d4d48af1c44a7ad2d5e'
    return url




if __name__ == "__main__":
    city_u = "Москва"
    url = get_url(city_u)

    print(url)
    pop.get_weather(url)
    pop.popodrobnee(city_u)





