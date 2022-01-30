from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('API')
mgr = owm.weather_manager()

place = input("Where do you want to see the weather?: ")

observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]

print("In " + place + " it is: " + w.detailed_status)
print ("Temperature is around: " + str(temp))

if temp < 10:
    print ("Wtf nigga thats cold")
elif temp < 20:
    print ("Aight thats fine")
else:
    print ("Warm")

