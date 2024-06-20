## encoding: utf-8

#__temp_comf = 25 ## число, которое должно получиться в сумме погоды и одежды
import clothe
import weather
import random
import messages


def get_weather(url):
    weather.weather_data(url)

    if weather.temperature_feels >= 20:
        print(random.choice(messages.hot))
        return random.choice(messages.hot)
    else:
        if weather.temperature_feels >= 15:
            print(random.choice(messages.warm))
            return random.choice(messages.warm)
        else:
            if weather.temperature_feels >= 7:
                print(random.choice(messages.mid))
                return random.choice(messages.mid)
            else:
                if weather.temperature_feels >= -20:
                    print(random.choice(messages.cold))
                    return random.choice(messages.cold)
                else:
                     print(random.choice(messages.dubak))
                     return random.choice(messages.dubak)
def popodrobnee(city):
    result = [
        'Сейчас в городе', city, str(weather.temperature), '°C',
        'Ощущается как', str(weather.temperature_feels), '°C',
        "min", str(weather.temperature_min), "max", str(weather.temperature_max), weather.sky
    ]
    return ' '.join(result)
