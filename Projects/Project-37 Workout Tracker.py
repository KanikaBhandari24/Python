import requests
from datetime import datetime
GENDER="female"
WEIGHT=43 
HEIGHT=158
AGE=18
text=input("Tell me which exercise you did: ")

param={ 
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}
header={ 
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY 
}

response=requests.post(url, json=param, headers=header)
result=response.json()
# print(result) 

GOOGLE_SHEET_NAME = "My Workouts"
today_date=datetime.now().strftime("%d/%m/%Y")
now_time=datetime.now().strftime("%X") 

for i in result["exercises"]:
    inputs={
        GOOGLE_SHEET_NAME : {
            "date": today_date,
            "time": now_time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"] 
        }
    }
    sheet=requests.post(
        sheet_endpoint, 
        json=inputs,
        auth=(
            USERNAME,
            PASSWORD,  
        ) 
    )
    print(f"Sheety Response: \n {sheet.text}")