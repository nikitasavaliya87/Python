
#
# print("ApI Application")
import requests

end="https://api.openweathermap.org/data/2.5/forecast"
api_key="083334a04b5674ede874e51dd8055ccf"
weather_param={
"lat":-37.813629,
"lon":144.963058,
"cnt":4,
"appid":api_key,

}
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
        print("Bring Umbrella")
