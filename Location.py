import requests

class Location():
    def __init__(self,IPKey):
        self.IPKey = IPKey
    def getLocation(self):
        r = requests.get('http://api.ipstack.com/check?access_key='+self.IPKey)
        r_json = r.json()

        return (r_json['zip'],r_json['country_code'],r_json['latitude'],r_json['longitude'])
