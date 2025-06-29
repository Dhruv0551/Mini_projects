import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def isAbove():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_data = response.json()    
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])
    if MY_LAT == iss_latitude and MY_LONG == iss_longitude:
        return True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}
def isSunset():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    user_data = response.json()
    sunrise = int(user_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(user_data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    if time_now > sunset and time_now < sunrise:
        return True

while True:
    time.sleep(60)
    if isAbove() and isSunset():
        with smtplib.SMTP("smtp.gmail.com") as emailConnection:
            emailConnection.starttls()
            emailConnection.login(user="Your Email",password="Your Password")
            emailConnection.sendmail(to_addrs="Target Addr",from_addr="Your Addr",msg="Your msg")
    else:
        print("Nuh uh")