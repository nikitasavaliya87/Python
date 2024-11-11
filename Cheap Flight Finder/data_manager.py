import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv(override=True)
sheety_endpoint=os.getenv("SHEETY_ENDPOINT")
class DataManager:
    def __init__(self):
        self.user=os.getenv("S_USERNAME")
        self.password=os.getenv("S_PASSWORD")
        self.authorization=HTTPBasicAuth(self.user, self.password)
        self.destination_data={}

    def get_destination_data(self):
        response=requests.get(url=sheety_endpoint, auth=self.authorization)
        data=response.json()
        self.destination_data=data["prices"]
        print(data)
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                auth=self.authorization
            )
            print(response.text)