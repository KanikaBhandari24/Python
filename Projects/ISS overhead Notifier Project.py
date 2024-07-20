import requests
from datetime import datetime
import smtplib
import time

LAT=28.521110
LONG=77.167160
Email="email dalo"
password="password dalo"

def iss_overhead():
    response=requests.get(url="http://api.open-notify.org/iss-now.json") 
    response.raise_for_status()
    data=response.json()

    latitude=float(data["iss_position"]["latitude"])
    longitude=float(data["iss_position"]["longitude"]) 

    #(lat-5=>28-5=>23) <= latitude <= (lat+5=>28+5=>33) same for longitute
    if LAT-5 <= latitude <= LAT+5 and LONG-5 <= longitude <= LONG+5:
        return True

def night():
    parameter={
        "lat": LAT,
        "lng": LONG,
        "formatted": 0,
    }
    response=requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data=response.json()
    sunrise=int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset=int(data["results"]["sunset"].split("T")[1].split(":")[0])

    timenow=datetime.now().hour
    if timenow >= sunset or timenow <=sunrise:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and night():
        connection=smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(Email, password)
        connection.sendmail(
            from_addr=Email,
            to_addrs=Email,
            msg="Subject:LOOK UP\nThe ISS is above you in the sky."
        )