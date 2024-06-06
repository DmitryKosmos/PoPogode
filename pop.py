## encoding: utf-8

#__temp_comf = 25 ## число, которое должно получиться в сумме погоды и одежды
import clothe
import weather
import random
import messages


def get_weather():
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
def popodrobnee():

    print('Сейчас в городе', weather.city, str(weather.temperature), '°C')
    print('Ощущается как', str(weather.temperature_feels), '°C')
    print("min", weather.temperature_min)
    print("max", weather.temperature_max)
    print(weather.sky)
    
    return 'Сейчас в городе', weather.city, str(weather.temperature), '°C','Ощущается как', str(weather.temperature_feels), '°C', "min", weather.temperature_min, "max", weather.temperature_max, weather.sky