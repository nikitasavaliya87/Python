
#
# print("ApI Application")
import requests
import os
from twilio.rest import Client



end="https://api.openweathermap.org/data/2.5/forecast"
api_key="083334a04b5674ede874e51dd8"
weather_param={
"lat":34.38,
"lon":58.20,
"cnt":4,
"appid":api_key,

}

account_sid = os.environ['sid']
auth_token = '[AuthToken]'



response=requests.get(end,params=weather_param)
#print(response.status_code)
response.raise_for_status()
weather_data=response.json()

#print(weather_data["list"][0]["weather"][0]['id'])
for data in weather_data["list"]:
    condition_code=data["weather"][0]["id"]
    #print(condition_code)
    if int(condition_code)<700:
        
        will_rain=True
    else:
        #print("Sunny")
        will_rain=False
    if will_rain:
        #print("Bring Umbrella")
        client = Client(account_sid, auth_token)
        # message = client.messages.create(
        #     body="Today is raining Day .... Remember to Bring an umbrella.",
        #     from_="+141523223",
        #     to="+61 11111111")
        # print (message)
        message = client.messages.create(
            from_='whatsapp:+141523223',
            content_sid='HXb5b62575e6e4ff6129ad7c8efe3e',
            content_variables='{Today is raining Day .... Remember to Bring an umbrella.}',
            to='whatsapp:+6111111111'
        )

