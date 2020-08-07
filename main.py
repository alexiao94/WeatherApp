from Location import Location
from Weather import Weather
from datetime import datetime
import time
weatherKey = 'XXXXXXXXXXXXX'
IPKey = 'XXXXXXXXXXX'
units = 'imperial'
syncTime = False;

while True:
    location = Location(IPKey).getLocation()
    weatherTime = Weather(weatherKey, location).getTime()
    actualWeather = Weather(weatherKey, location).getWeather()
    actualTime = datetime.now()
    forcastTime = datetime.fromtimestamp(Weather(weatherKey, location).getForecast(units, 1)[0])
    forcastWeather = Weather(weatherKey, location).getForecast(units, 1)[1][0]['main']
    print('Real time: '+str(actualTime))
    print('App time: '+str(weatherTime))
    print('Current weather:'+actualWeather)
    print('Forecast time: '+str(forcastTime))
    print('Forecast Weather: '+forcastWeather)


    if forcastWeather == 'Rain':
        print('Bring Umbrella\n')
    elif forcastWeather == 'Clouds':
        print('Enjoy the cloudy weather!\n')
    elif forcastWeather == 'Clear':
        print('Nice weather!\n')
    else:
        print(forcastWeather)
    if syncTime:
        print(actualTime)
        print('Time is sync')
        reTime=3600
    else:
        reTime = forcastTime-actualTime
        syncTime == True

    if reTime.total_seconds()>1800:
        print(reTime.total_seconds()-1800)
        time.sleep(reTime.total_seconds()-1800)
    else:
        print(reTime.total_seconds())
        time.sleep(reTime.total_seconds())

    count += 1
    if count == 5:
        print('End of program')
        break
