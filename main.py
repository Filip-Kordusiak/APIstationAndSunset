import requests
import json
from datetime import datetime

MY_LAT = 52.229675
MY_LNG = 21.012230

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()


x = response.json()
print(x)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG
}

response1 = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LNG}&formatted=0")
response1.raise_for_status()
y = response1.json()
sunset = y['results']['sunrise']
print(sunset.split("T")[1].split(":")[0])#podzielone na czesci dzieki czemu bedzie mozna łatwo wyswitlic wszystko
time_now = datetime.now()
print(time_now.hour)


