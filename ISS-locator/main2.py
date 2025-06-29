import requests
import datetime as dt

MY_LAT = 23.02579000
MY_LONG = 72.58727000

user_params = {
    "lat":MY_LAT,
    "lng":MY_LONG,
    "formatted":0
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=user_params)
response.raise_for_status()

user_data = response.json()

sunrise = user_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = user_data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunset)
print(sunrise)

currentTime = dt.datetime.now().hour
print(currentTime)