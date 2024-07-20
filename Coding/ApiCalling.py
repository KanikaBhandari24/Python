import requests
from datetime import datetime

#LEARNING API CALLING
response=requests.get(url="http://api.open-notify.org/iss-now.json") 
#RAISES THE TYPE OF STATUS
response.raise_for_status()
# data=response.json()["iss_position"]["longitude"] # available keys set in -> [][]
# print(data)

data=response.json()
longitude=data["iss_position"]["longitude"]
latitude=data["iss_position"]["latitude"]
iss_position = (longitude, latitude)
print(iss_position)

print(response)
print(response.status_code) 

if response.status_code == 404:
    raise Exception("That resourse does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to its access") 


#SUNSET SUNRISE API CALLING
LAT=28.521110
LONG=77.167160
parameter={
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}
response=requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data=response.json()
sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
timenow=datetime.now()
print(timenow.hour)