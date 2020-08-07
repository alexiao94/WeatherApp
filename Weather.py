import requests
from datetime import datetime

class Weather():
    def __init__(self,weatherKey,location):
        self.weatherKey = weatherKey
        self.location = location
        self.zip = self.location[0]
        self.country = self.location[1]
        self.latitude = str(self.location[2])
        self.longitude = str(self.location[3])

    def getWeather(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+self.zip+','+self.country+'&appid='+self.weatherKey)
        r_json = r.json()
        return r_json['weather'][0]['main']
    def getTemperature(self,units):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + self.zip + ',' + self.country + '&units='+units+'&appid=' + self.weatherKey)
        r_json = r.json()
        return r_json['main']
    def getTime(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=' + self.zip + ',' + self.country + '&appid=' + self.weatherKey)
        r_json = r.json()
        return datetime.fromtimestamp(r_json['dt'])
    def getForecast(self,units,x):
        r = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat='+self.latitude+'&lon='+self.longitude+'&units='+units+'&exclude=minutely,daily&appid='+self.weatherKey)
        r_json = r.json()
        return (r_json['hourly'][x]['dt'],r_json['hourly'][x]['weather'])

