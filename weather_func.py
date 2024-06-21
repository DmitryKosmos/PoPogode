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

correct_cities = {
    "москва": "Москва",
    "санкт-петербург": "Санкт-Петербург",
    "новосибирск": "Новосибирск",
    "екатеринбург": "Екатеринбург",
    "нижний новгород": "Нижний Новгород",
    "казань": "Казань",
    "челябинск": "Челябинск",
    "омск": "Омск",
    "самара": "Самара",
    "ростов-на-дону": "Ростов-на-Дону",
    "уфа": "Уфа",
    "красноярск": "Красноярск",
    "пермь": "Пермь",
    "воронеж": "Воронеж",
    "волгоград": "Волгоград",
    "краснодар": "Краснодар",
    "саратов": "Саратов",
    "тюмень": "Тюмень",
    "тольятти": "Тольятти",
    "ижевск": "Ижевск",
    "барнаул": "Барнаул",
    "ульяновск": "Ульяновск",
    "иркутск": "Иркутск",
    "хабаровск": "Хабаровск",
    "ярославль": "Ярославль",
    "владивосток": "Владивосток",
    "махачкала": "Махачкала",
    "томск": "Томск",
    "оренбург": "Оренбург",
    "кемерово": "Кемерово",
    "новокузнецк": "Новокузнецк",
    "рязань": "Рязань",
    "астрахань": "Астрахань",
    "набережные челны": "Набережные Челны",
    "пенза": "Пенза",
    "липецк": "Липецк",
    "киров": "Киров",
    "магнитогорск": "Магнитогорск",
    "тверь": "Тверь",
    "брянск": "Брянск",
    "иваново": "Иваново",
    "курск": "Курск",
    "севастополь": "Севастополь",
    "белгород": "Белгород",
    "сочи": "Сочи",
    "калининград": "Калининград",
    "симферополь": "Симферополь",
    "владикавказ": "Владикавказ",
    "ставрополь": "Ставрополь",
    "нижний тагил": "Нижний Тагил",
    "архангельск": "Архангельск",
    "калуга": "Калуга",
    "сургут": "Сургут",
    "орел": "Орёл",
    "череповец": "Череповец",
    "владимир": "Владимир",
    "чебоксары": "Чебоксары",
    "смоленск": "Смоленск",
    "волжский": "Волжский",
    "муром": "Муром",
    "энгельс": "Энгельс",
    "якутск": "Якутск",
    "курган": "Курган",
    "таганрог": "Таганрог",
    "петрозаводск": "Петрозаводск",
    "саранск": "Саранск",
    "тула": "Тула",
    "братск": "Братск",
    "дзержинск": "Дзержинск",
    "димитровград": "Димитровград",
    "нижневартовск": "Нижневартовск",
    "новороссийск": "Новороссийск",
    "химки": "Химки",
    "балашиха": "Балашиха",
    "королев": "Королёв",
    "коломна": "Коломна",
    "подольск": "Подольск",
    "серпухов": "Серпухов",
    "орехово-зуево": "Орехово-Зуево",
    "копейск": "Копейск",
    "нижнекамск": "Нижнекамск",
    "первоуральск": "Первоуральск",
    "сызрань": "Сызрань",
    "норильск": "Норильск",
    "армавир": "Армавир",
    "благовещенск": "Благовещенск",
    "чита": "Чита",
    "южно-сахалинск": "Южно-Сахалинск",
    "ангарск": "Ангарск",
    "старый оскол": "Старый Оскол",
    "березники": "Березники",
    "миасс": "Миасс",
    "прокопьевск": "Прокопьевск",
    "одинцово": "Одинцово",
    "щелково": "Щёлково",
    "нальчик": "Нальчик",
    "псков": "Псков",
    "сергиев посад": "Сергиев Посад",
    "невинномысск": "Невинномысск",
    "абакан": "Абакан",
    "великий новгород": "Великий Новгород",
    "грозный": "Грозный",
    "йошкар-ола": "Йошкар-Ола",
    "кострома": "Кострома",
    "комсомольск-на-амуре": "Комсомольск-на-Амуре",
    "магадан": "Магадан",
    "майкоп": "Майкоп",
    "находка": "Находка",
    "новочебоксарск": "Новочебоксарск",
    "новомосковск": "Новомосковск",
    "новошахтинск": "Новошахтинск",
    "петропавловск-камчатский": "Петропавловск-Камчатский",
    "северск": "Северск",
    "стерлитамак": "Стерлитамак",
    "сыктывкар": "Сыктывкар",
    "тобольск": "Тобольск",
    "улан-удэ": "Улан-Удэ",
    "уссурийск": "Уссурийск",
    "шахты": "Шахты",
    "электросталь": "Электросталь"
}






