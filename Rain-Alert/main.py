import requests
from twilio.rest import Client
import os



account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")


api_key = os.environ.get("my_api")
lat=23.02579
lon = 72.58727

apiReq = "https://api.openweathermap.org/data/2.5/forecast"

api_params = {
    "lat": lat,
    "lon": lon,
    "cnt":4,
    "appid": api_key
}

response = requests.get(apiReq,params=api_params)
response.raise_for_status()
weather_data = response.json()

isRaining = False
for i in weather_data["list"]:
    if i["weather"][0]["id"]<700:
        isRaining = True


if isRaining:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Sup Nigga",
    to='+919328403727',
    from_="+1 267 837 5340"
)
    print(message.status)