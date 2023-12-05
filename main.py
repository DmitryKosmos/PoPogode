##__temp_comf = 25 ## число, которое должно получиться в сумме погоды и одежды

import  weather
import  clothe
import random
import messages


if weather.temperature_feels >= 20:
    print(random.choice(messages.hot))
else:
    if weather.temperature_feels >= 15:
        print(random.choice(messages.warm))
    else:
        if weather.temperature_feels >= 7:
            print(random.choice(messages.mid))
        else:
            if weather.temperature_feels >= -20:
                print(random.choice(messages.cold))
            else:
                 print(random.choice(messages.dubak))

print('Сейчас в городе', weather.city, str(weather.temperature), '°C')
print('Ощущается как', str(weather.temperature_feels), '°C')
print("min", weather.temperature_min)
print("max", weather.temperature_max)
print(weather.sky)
