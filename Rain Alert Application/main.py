
#
# print("ApI Application")
import requests

end="https://api.openweathermap.org/data/2.5/forecast"
api_key="083334a04b5674ede874e51dd8055ccf"
weather_param={
"lat":-37.813629,
"lon":144.963058,
"appid":api_key,

}
response=requests.get(end,params=weather_param)
#print(response.status_code)
print(response.json())