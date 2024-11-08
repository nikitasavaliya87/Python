import requests
from datetime import datetime
import os
from dotenv import load_dotenv,dotenv_values

load_dotenv(override=True)

APP_ID=os.getenv("APP_ID")



API_KEY =os.getenv("API_KEY")
TOKEN=os.getenv("TOKEN")
GENDER="Female"
WEIGHT_KG="80"
HEIGHT_CM="128"
AGE="37"

nutrionix_endpoint= os.getenv("nutrionix_endpoint")
text=input("Tell me which exercise You did it:")

header={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
    }
param={
    "query":text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}
response=requests.post(url=nutrionix_endpoint, json=param,headers=header)
result=response.json()
print(result)


sheety_endpoint=os.getenv("sheety_endpoint")

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # Not authentication
    #sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

   # print(sheet_response.text)
    #basic Authentication
    sheet_response=requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(os.getenv("USER"),os.getenv("PSWD")

        )
    )

    #Bearer Token Uthentication 
    bearer_header={
        "Authorization":f"Bearer {TOKEN}"
    }
    sheet_response=requests.post(
        sheety_endpoint,
            json=sheet_inputs,
               headers=header
    )